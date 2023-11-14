from jproperties import Properties
import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

configs = Properties()
with open('./resource/application.properties', 'rb') as config_file:
    configs.load(config_file)

upbitKey = configs.get('UPBIT_KEY').data
upbitSecret = configs.get('UPBIT_SECRET').data

UPBIT_HOST = 'https://api.upbit.com'

payload = {
    'access_key': upbitKey,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, upbitSecret)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
    'Authorization': authorization,
}

# 계좌 조회
response = requests.get(UPBIT_HOST + '/v1/accounts', headers=headers)
data = response.json()

# 종목 조회
url = UPBIT_HOST + '/v1/market/all?isDetails=false'
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

for row in response.json():
    print(row)

# 호가 정보 조회
# https://docs.upbit.com/reference/%ED%98%B8%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C

url = UPBIT_HOST + '/v1/orderbook'
headers = {"accept": "application/json"}
params = {"markets" : ['KRW-BTC']}
response = requests.get(url, params=params, headers=headers)
print(response.json())

# 시세 체결 조회
# https://docs.upbit.com/reference/%EC%B5%9C%EA%B7%BC-%EC%B2%B4%EA%B2%B0-%EB%82%B4%EC%97%AD

url = UPBIT_HOST + '/v1/trades/ticks'
headers = {"accept": "application/json"}
params = {"market": "KRW-BTC", "count": 10}
response = requests.get(url, params=params, headers=headers)
print(response.json())

# 시세 현재가(Ticker) 조회
# https://docs.upbit.com/reference/ticker%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4

url = UPBIT_HOST + '/v1/trades/v1/ticker'
headers = {"accept": "application/json"}
params = {"markets" : ['KRW-BTC']}
print(response.json())





