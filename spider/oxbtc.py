import requests
from .ut import logger
import time, json

s = requests.Session()
s.headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

merchant = "0xbtc"


@logger.catch
def getdata():
    url = "https://www.oxbtc.com/api/default/shop?buy_page=true"
    logger.info(f"get contract list {url}")
    z1 = s.get(url)
    data = z1.json()
    datas = []
    if data["Code"] == "0":
        contracts = data["Data"]["contracts"]["contracts"]
        for contract in contracts:
            datas.append(getcontract(contract))
        return datas


@logger.catch
def getcontract(contract):
    url = f"https://www.oxbtc.com/api/default/contract_detail?symbol={contract}"
    logger.info(f"get contract: {contract}")

    z1 = s.get(url)
    data = z1.json()
    if data["Code"] == "0":
        return data["Data"]


if __name__ == "__main__":
    data = getdata()
    with open(f"demo/{merchant}.json", "w") as f:
        f.write(json.dumps(data))
