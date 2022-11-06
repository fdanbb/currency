import requests

btcUrl = 'https://cex.io/api/last_price/BTC/USD'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def main():
    print(getBTCPrice())


def getBTCPrice():
    response = requests.get(btcUrl, headers=headers)
    return response.json().get("lprice")
