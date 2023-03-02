from typing import Union
from pydantic import BaseModel, Field


class Tracking(BaseModel):
    title: Union[str, None] = None
    address_list: set[str, None] = None
    amounts: float = Field(default=0, description="digit 4")


class Tokens(BaseModel):
    name: str
    decimals: int
    contract_address: str
    chains: str
    address: list[Tracking, None] = []

    class Config:
        schema_extra = {
            "example": {
                "name": "ETH",
                "decimals": 18,
                "contract_address": "0x000000000000000",
                "chains": "ETH",
                "address": [
                    {
                        "title": "Foundation",
                        "address_list": ["0x00000000000000", "0x00000000000001"],
                        "amounts": 0.0
                    },
                ]
            }
        }
