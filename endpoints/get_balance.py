# encoding: utf-8

from fastapi import Path, HTTPException
from pydantic import BaseModel

from constants import ADDRESS_EXAMPLE, REGEX_ANUMA_ADDRESS
from server import app, anumad_client


class BalanceResponse(BaseModel):
    address: str = ADDRESS_EXAMPLE
    balance: int = 38240000000


@app.get("/addresses/{anumaAddress}/balance", response_model=BalanceResponse, tags=["Anuma addresses"])
async def get_balance_from_anuma_address(
        anumaAddress: str = Path(
            description=f"Anuma address as string e.g. {ADDRESS_EXAMPLE}",
            regex=REGEX_ANUMA_ADDRESS)):
    """
    Get balance for a given anuma address
    """
    resp = await anumad_client.request("getBalanceByAddressRequest",
                                       params={
                                           "address": anumaAddress
                                       })

    try:
        resp = resp["getBalanceByAddressResponse"]
    except KeyError:
        if "getUtxosByAddressesResponse" in resp and "error" in resp["getUtxosByAddressesResponse"]:
            raise HTTPException(status_code=400, detail=resp["getUtxosByAddressesResponse"]["error"])
        else:
            raise

    try:
        balance = int(resp["balance"])

    # return 0 if address is ok, but no utxos there
    except KeyError:
        balance = 0

    return {
        "address": anumaAddress,
        "balance": balance
    }
