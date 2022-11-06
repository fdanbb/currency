from decimal import Decimal

import requests

koronaLiraUrl = 'https://koronapay.com/transfers/online/api/transfers/tariffs?receivingAmount=1000&alternatives=false&sendingCurrencyId=810&receivingCurrencyId=949&sendingCountryId=RUS&receivingCountryId=TUR&receivingMethod=cash&paymentMethod=debitCard'
koronaUsdUrl = 'https://koronapay.com/transfers/online/api/transfers/tariffs?receivingAmount=1000&alternatives=false&sendingCurrencyId=810&receivingCurrencyId=840&sendingCountryId=RUS&receivingCountryId=TUR&receivingMethod=cash&paymentMethod=debitCard'
koronaEuroUrl = 'https://koronapay.com/transfers/online/api/transfers/tariffs?receivingAmount=100&alternatives=false&sendingCurrencyId=810&receivingCurrencyId=978&sendingCountryId=RUS&receivingCountryId=TUR&receivingMethod=cash&paymentMethod=debitCard'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def getLiraPrice():
    response = requests.get(koronaLiraUrl, headers=headers)
    return round((Decimal(response.json()[0].get("exchangeRate"))), 2)


def getUsdPrice():
    response = requests.get(koronaUsdUrl, headers=headers)
    return round((Decimal(response.json()[0].get("exchangeRate"))), 2)


def getEuroPrice():
    response = requests.get(koronaEuroUrl, headers=headers)
    return round((Decimal(response.json()[0].get("exchangeRate"))), 2)
