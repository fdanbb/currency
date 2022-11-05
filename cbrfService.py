from decimal import Decimal

import requests
import xml.etree.ElementTree as ET

url = 'https://www.cbr.ru/scripts/XML_daily.asp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def getLiraPrice():
    response = requests.get(url, headers=headers)
    root = ET.fromstring(response.content)

    for valute in root.findall("Valute"):
        if valute.items()[0][1] == 'R01700J':
            nominal = valute.find('Nominal').text
            value = valute.find('Value').text
            return Decimal(value.replace(',', '.')) / int(nominal)


def getUsdPrice():
    response = requests.get(url, headers=headers)
    root = ET.fromstring(response.content)

    for valute in root.findall("Valute"):
        if valute.items()[0][1] == 'R01235':
            nominal = valute.find('Nominal').text
            value = valute.find('Value').text
            return Decimal(value.replace(',', '.')) / int(nominal)


def getEuroPrice():
    response = requests.get(url, headers=headers)
    root = ET.fromstring(response.content)

    for valute in root.findall("Valute"):
        if valute.items()[0][1] == 'R01239':
            nominal = valute.find('Nominal').text
            value = valute.find('Value').text
            return Decimal(value.replace(',', '.')) / int(nominal)
