# encoding: utf-8
from typing import List

from pydantic import BaseModel

from server import app, anumad_client


class BlockdagResponse(BaseModel):
    networkName: str = "anuma-mainnet"
    blockCount: str = "195"
    headerCount: str = "195"
    tipHashes: List[str] = ["6c405a4670e02bafd5658a2aa49618467cc8c7691ca87538e553cec0998127e6"]
    difficulty: float = 65536.01
    pastMedianTime: str = "1725139204875"
    virtualParentHashes: List[str] = ["6c405a4670e02bafd5658a2aa49618467cc8c7691ca87538e553cec0998127e6"]
    pruningPointHash: str = "f872dffba6648e8bfcb4f8c319015b41d2c8562e87605d95d906c5c5a2f6ce6f",
    virtualDaaScore: str = "194"


@app.get("/info/blockdag", response_model=BlockdagResponse, tags=["Anuma network info"])
async def get_blockdag():
    """
    Get some global Anuma BlockDAG information
    """
    resp = await anumad_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
