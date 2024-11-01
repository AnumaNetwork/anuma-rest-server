# encoding: utf-8
import os
from fastapi import Path, HTTPException
from pydantic import BaseModel
from typing import List

from constants import REGEX_ANUMA_ADDRESS, ADDRESS_EXAMPLE
from server import app, anumad_client


class OutpointModel(BaseModel):
    transactionId: str = "ef62efbc2825d3ef9ec1cf9b80506876ac077b64b11a39c8ef5e028415444dc9"
    index: int = 0


class ScriptPublicKeyModel(BaseModel):
    scriptPublicKey: str = "20c5629ce85f6618cd3ed1ac1c99dc6d3064ed244013555c51385d9efab0d0072fac"


class UtxoModel(BaseModel):
    amount: str = "11501593788",
    scriptPublicKey: ScriptPublicKeyModel
    blockDaaScore: str = "18867232"
    isCoinbase: bool = False


class UtxoResponse(BaseModel):
    address: str = ADDRESS_EXAMPLE
    outpoint: OutpointModel
    utxoEntry: UtxoModel


@app.get("/addresses/{anumaAddress}/utxos", response_model=List[UtxoResponse], tags=["Anuma addresses"])
async def get_utxos_for_address(anumaAddress: str = Path(
    description=f"Anuma address as string e.g. {ADDRESS_EXAMPLE}",
    regex=REGEX_ANUMA_ADDRESS)):
    """
    Lists all open utxo for a given anuma address
    """
    resp = await anumad_client.request("getUtxosByAddressesRequest",
                                       params={
                                           "addresses": [anumaAddress]
                                       }, timeout=120)
    try:
        return (utxo for utxo in resp["getUtxosByAddressesResponse"]["entries"] if utxo["address"] == anumaAddress)
    except KeyError:
        if "getUtxosByAddressesResponse" in resp and "error" in resp["getUtxosByAddressesResponse"]:
            raise HTTPException(status_code=400, detail=resp["getUtxosByAddressesResponse"]["error"])
        else:
            return []
