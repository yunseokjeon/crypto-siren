import websockets
from jproperties import Properties
import jwt  # PyJWT
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote
import websocket  # websocket-client
from multiprocessing import Process
import asyncio
import datetime

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
# response = requests.get(UPBIT_HOST + '/v1/accounts', headers=headers)
# data = response.json()

# 종목 조회
# url = UPBIT_HOST + '/v1/market/all?isDetails=false'
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
#
# for row in response.json():
#     print(row)

# 호가 정보 조회
# https://docs.upbit.com/reference/%ED%98%B8%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C

# url = UPBIT_HOST + '/v1/orderbook'
# headers = {"accept": "application/json"}
# params = {"markets" : ['KRW-BTC']}
# response = requests.get(url, params=params, headers=headers)
# print(response.json())

# 시세 체결 조회
# https://docs.upbit.com/reference/%EC%B5%9C%EA%B7%BC-%EC%B2%B4%EA%B2%B0-%EB%82%B4%EC%97%AD

# url = UPBIT_HOST + '/v1/trades/ticks'
# headers = {"accept": "application/json"}
# params = {"market": "KRW-BTC", "count": 10}
# response = requests.get(url, params=params, headers=headers)
# print(response.json())

# 시세 현재가(Ticker) 조회
# https://docs.upbit.com/reference/ticker%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4

# url = UPBIT_HOST + '/v1/ticker'
# headers = {"accept": "application/json"}
# params = {"markets" : ['KRW-BTC']}
# response = requests.get(url, params=params, headers=headers)
# print(response.json())

# WebSocket

def socket():
    def on_message(ws, message):
        # do something
        data = message.decode('utf-8')
        print(data)

    def on_connect(ws):
        print("connected!")
        # Request after connection
        # ws.send(f'[{{"ticket":""}},{{"type":"orderbook","codes":["{code}"]}}]')

        # ws.send('[{"ticket":"test example"},{"type":"ticker","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')

        ws.send('[{"ticket":"test example"},{"type":"trade","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')

        # ws.send('[{"ticket":"test example"},{"type":"orderbook","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')

    def on_error(ws, err):
        print(err)

    def on_close(ws, status_code, msg):
        print("closed!")

    ws_app = websocket.WebSocketApp("wss://api.upbit.com/websocket/v1",
                                    header=headers,
                                    on_message=on_message,
                                    on_open=on_connect,
                                    on_error=on_error,
                                    on_close=on_close)
    ws_app.run_forever()


if __name__ == "__main__":
    socket()

'''
https://docs.upbit.com/v1.4.0/reference/websocket-ticker

ticker :

{   "type":"ticker",
    "code":"KRW-BTC",
    "opening_price":49190000.0000,
    "high_price":49200000.0000,
    "low_price":49023000.0000,
    "trade_price":49053000.0000,
    "prev_closing_price":49165000.00000000,
    "acc_trade_price":12747895025.205850000000,
    "change":"FALL",
    "change_price":112000.00000000,
    "signed_change_price":-112000.00000000,
    "change_rate":0.0022780433,
    "signed_change_rate":-0.0022780433,
    "ask_bid":"ASK",
    "trade_volume":0.01605655,
    "acc_trade_volume":259.61033542,
    "trade_date":"20231119",
    "trade_time":"033042",
    "trade_timestamp":1700364642227,
    "acc_ask_volume":157.18779616,
    "acc_bid_volume":102.42253926,
    "highest_52_week_price":50652000.0000,
    "highest_52_week_date":"2023-11-16",
    "lowest_52_week_price":20700000.00000000,
    "lowest_52_week_date":"2022-12-30",
    "market_state":"ACTIVE",
    "is_trading_suspended":false,
    "delisting_date":null,
    "market_warning":"NONE",
    "timestamp":1700364642247,
    "acc_trade_price_24h":85934950517.43824000,
    "acc_trade_volume_24h":1749.53713304,
    "stream_type":"SNAPSHOT"
}

{   "type":"ticker",
    "code":"KRW-BTC",
    "opening_price":49190000.0000,
    "high_price":49200000.0000,
    "low_price":49023000.0000,
    "trade_price":49053000.0000,
    "prev_closing_price":49165000.00000000,
    "acc_trade_price":12749660933.205850000000,
    "change":"FALL",
    "change_price":112000.00000000,
    "signed_change_price":-112000.00000000,
    "change_rate":0.0022780433,
    "signed_change_rate":-0.0022780433,
    "ask_bid":"ASK",
    "trade_volume":0.03600000,
    "acc_trade_volume":259.64633542,
    "trade_date":"20231119",
    "trade_time":"033048",
    "trade_timestamp":1700364648886,
    "acc_ask_volume":157.22379616,
    "acc_bid_volume":102.42253926,
    "highest_52_week_price":50652000.0000,
    "highest_52_week_date":"2023-11-16",
    "lowest_52_week_price":20700000.00000000,
    "lowest_52_week_date":"2022-12-30",
    "market_state":"ACTIVE",
    "is_trading_suspended":false,
    "delisting_date":null,
    "market_warning":"NONE",
    "timestamp":1700364648910,
    "acc_trade_price_24h":85934950517.43824000,
    "acc_trade_volume_24h":1749.53713304,
    "stream_type":"REALTIME"
}
'''

'''
https://docs.upbit.com/v1.4.0/reference/websocket-trade

trade :

{   "type":"trade",
    "code":"KRW-BTC",
    "timestamp":1700365434203,
    "trade_date":"2023-11-19",
    "trade_time":"03:43:54",
    "trade_timestamp":1700365434170,
    "trade_price":49083000.0000,
    "trade_volume":0.02100531,
    "ask_bid":"ASK",
    "prev_closing_price":49165000.00000000,
    "change":"FALL",
    "change_price":82000.00000000,
    "sequential_id":1700365434170000,
    "stream_type":"SNAPSHOT"
}

{   "type":"trade",
    "code":"KRW-BTC",
    "timestamp":1700365437515,
    "trade_date":"2023-11-19",
    "trade_time":"03:43:57",
    "trade_timestamp":1700365437486,
    "trade_price":49083000.0000,
    "trade_volume":0.02430412,
    "ask_bid":"ASK",
    "prev_closing_price":49165000.00000000,
    "change":"FALL",
    "change_price":82000.00000000,
    "sequential_id":1700365437486000,
    "stream_type":"REALTIME"
}
'''

'''
https://docs.upbit.com/v1.4.0/reference/websocket-orderbook

orderbook :

{   "type":"orderbook",
    "code":"KRW-BTC",
    "timestamp":1700365596191,
    "total_ask_size":4.28974217,
    "total_bid_size":1.73187493,
    "orderbook_units":[
            {"ask_price":4.912E7,"bid_price":4.909E7,"ask_size":0.00697849,"bid_size":0.00059027},
            {"ask_price":4.9121E7,"bid_price":4.9089E7,"ask_size":0.90941507,"bid_size":0.53841327},
            {"ask_price":4.9123E7,"bid_price":4.9088E7,"ask_size":0.01247002,"bid_size":0.38576567},
            {"ask_price":4.9125E7,"bid_price":4.9087E7,"ask_size":0.01530151,"bid_size":0.00789262},
            {"ask_price":4.9132E7,"bid_price":4.9086E7,"ask_size":0.03873100,"bid_size":0.21323551},
            {"ask_price":4.9137E7,"bid_price":4.9083E7,"ask_size":0.0031329,"bid_size":0.24212526},
            {"ask_price":4.9138E7,"bid_price":4.9082E7,"ask_size":0.10957738,"bid_size":0.00613558},
            {"ask_price":4.9141E7,"bid_price":4.908E7,"ask_size":0.04635187,"bid_size":0.01559423},
            {"ask_price":4.9142E7,"bid_price":4.9079E7,"ask_size":0.02034920,"bid_size":0.03575763},
            {"ask_price":4.9146E7,"bid_price":4.9078E7,"ask_size":0.098,"bid_size":0.00545050},
            {"ask_price":4.915E7,"bid_price":4.9076E7,"ask_size":0.28373194,"bid_size":0.00407531},
            {"ask_price":4.9151E7,"bid_price":4.9075E7,"ask_size":0.08286282,"bid_size":0.04627734},
            {"ask_price":4.9152E7,"bid_price":4.907E7,"ask_size":0.0399,"bid_size":0.03797772},
            {"ask_price":4.9163E7,"bid_price":4.9069E7,"ask_size":2.61019119,"bid_size":0.19226482},
            {"ask_price":4.9164E7,"bid_price":4.9068E7,"ask_size":0.01274878,"bid_size":0.00031920}
            ],
    "stream_type":"SNAPSHOT"
}

{   "type":"orderbook","code":
    "KRW-BTC",
    "timestamp":1700365598352,
    "total_ask_size":1.68950135,
    "total_bid_size":1.73187493,
    "orderbook_units":[
        {"ask_price":4.912E7,"bid_price":4.909E7,"ask_size":0.00748776,"bid_size":0.00059027},
        {"ask_price":4.9121E7,"bid_price":4.9089E7,"ask_size":0.90565682,"bid_size":0.53841327},
        {"ask_price":4.9123E7,"bid_price":4.9088E7,"ask_size":0.01247002,"bid_size":0.38576567},
        {"ask_price":4.9125E7,"bid_price":4.9087E7,"ask_size":0.01530151,"bid_size":0.00789262},
        {"ask_price":4.9131E7,"bid_price":4.9086E7,"ask_size":0.0119,"bid_size":0.21323551},
        {"ask_price":4.9132E7,"bid_price":4.9083E7,"ask_size":0.03873100,"bid_size":0.24212526},
        {"ask_price":4.9135E7,"bid_price":4.9082E7,"ask_size":0.0275,"bid_size":0.00613558},
        {"ask_price":4.9137E7,"bid_price":4.908E7,"ask_size":0.0031329,"bid_size":0.01559423},
        {"ask_price":4.9138E7,"bid_price":4.9079E7,"ask_size":0.10957738,"bid_size":0.03575763},
        {"ask_price":4.9141E7,"bid_price":4.9078E7,"ask_size":0.03290000,"bid_size":0.00545050},
        {"ask_price":4.9142E7,"bid_price":4.9076E7,"ask_size":0.02034920,"bid_size":0.00407531},
        {"ask_price":4.9146E7,"bid_price":4.9075E7,"ask_size":0.098,"bid_size":0.04627734},
        {"ask_price":4.915E7,"bid_price":4.907E7,"ask_size":0.28373194,"bid_size":0.03797772},
        {"ask_price":4.9151E7,"bid_price":4.9069E7,"ask_size":0.08286282,"bid_size":0.19226482},
        {"ask_price":4.9152E7,"bid_price":4.9068E7,"ask_size":0.0399,"bid_size":0.00031920}],
        "stream_type":"REALTIME"
}
'''
