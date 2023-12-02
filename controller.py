import datetime

import requests
from time import sleep

from model.ticker import create



INTERVAL = 3


def fetch():
    url = 'https://coincheck.com/api/order_book'
    resp = requests.get(url).json()
    print(resp)
    timestamp = datetime.datetime.fromtimestamp(resp['timestamp'])


def run():
    while True:
        fetch()
        sleep(1)

