from fastapi import FastAPI, HTTPException
from crypto_token import *
from chain_checker import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/tk/create')
async def create_tokens(new_token: Tokens):
    check_token_chain = new_token.dict()
    check = await token_exists(check_token_chain["contract_address"], check_token_chain["chains"])

    # Klaytn
    if check_token_chain["chains"] == "KLAYTN":
        if check["symbol"] == check_token_chain["name"]:
            return check
        else:
            return HTTPException(status_code=400, detail="Not Valid Symbol and Contact address")
    # Others
    else:
        if check["status"] == "1" and check["result"] != "0":
            return check


tk_items = {
"klay1": {
  "name": "KLAY1",
  "decimals": 18,
  "contract_address": "0x000000000000000",
  "chains": "KLAYTN",
  "address": [{
    "title": "Big1",
    "address_list": [
      "0x00000000000000",
      "0x00000000000001"
    ],
    "amounts": 133333330
  }]
},
"eth1": {
  "name": "ETH1",
  "decimals": 18,
  "contract_address": "0x000000000000000",
  "chains": "ETH",
  "address": [{
    "title": "BIG2",
    "address_list": [
      "0x00000000000000",
      "0x00000000000001"
    ],
    "amounts": 133555333330
  }]
},

}

@app.get('/tk/{token_name}', response_model=Tokens)
async def get_tokens(token_name: str):
    return tk_items[token_name]