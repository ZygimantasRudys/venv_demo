from requests import get
from requests import Response

if __name__ == '__main__':
    resp: Response = get("https://lrytas.lt")
    print(f"{resp.status_code}")
    # print(f"{resp.text}")