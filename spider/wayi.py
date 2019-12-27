import requests
from .ut import logger
import time, json

s = requests.Session()
s.headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

merchant = "wayi"


@logger.catch
def getdata():
    url = "https://api.wayi.cn/hash/getHashPlan/multi"
    logger.info(f"get url {url}")
    pageNO = 1
    ret_data = []
    while True:
        logger.info(f"get page {pageNO}")
        reqData = {
            "pageNO": pageNO,
            "pageSize": 10,
            "search": '{"coinType":"2","status":1,"productType":"110","hash_status":1}',
        }
        z1 = s.post(url, json=reqData)
        data = z1.json()["body"]
        if z1.json()["type"]:
            ret_data.extend(data["result"].copy())
            if data["pageTotal"] > data["pageNum"]:
                pageNO = data["pageNum"] + 1
                continue
        break
    return ret_data


if __name__ == "__main__":
    data = getdata()
    with open(f"demo/{merchant}.json", "w") as f:
        f.write(json.dumps(data))
