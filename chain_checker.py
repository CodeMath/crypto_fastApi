import requests
import os


async def token_exists(ct, chains):
    if chains == "KLAYTN":
        klay_base = "https://kip7-api.klaytnapi.com/v1/contract/%s" % ct
        res = requests.get(
            klay_base, auth=(os.environ["klaytn_id"], os.environ["klaytn_pw"]),
            headers={"x-chain-id": "8217"}
        ).json()
        return res
    else:
        if chains == "ETH":
            base = "https://api.etherscan.io/"
            api_key = os.environ["etherscan"]
        elif chains == "POLYGON":
            base = "https://api.polygonscan.com/"
            api_key = os.environ["polygon"]
        elif chains == "BSC":
            base = "https://api.bscscan.com/"
            api_key = os.environ["bsc"]
        else:
            return "None"
        api_param = "api??module=stats&action=tokensupply&contractaddress={}&apikey={}" \
            .format(ct, api_key)
        res = requests.get(
            base + api_param
        ).json()

        return res