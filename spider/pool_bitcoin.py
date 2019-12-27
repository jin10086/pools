import requests
from .ut import logger
import time, json

s = requests.Session()
s.headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

merchant = "pool_bitcoin"


@logger.catch
def getdata():
    url = "https://console.pool.bitcoin.com/srv/getcontracts?coin=profit"
    logger.info(f"get page {url}")
    z1 = s.get(url)
    data = z1.json()
    return data


if __name__ == "__main__":
    data = getdata()
    with open(f"demo/{merchant}.json", "w") as f:
        f.write(json.dumps(data))
