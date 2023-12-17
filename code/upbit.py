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
import threading

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


class SocketClient1(threading.Thread):
    def __init__(self):
        super().__init__()
        self.url = "wss://api.upbit.com/websocket/v1"
        self.ws = websocket.WebSocketApp(
            url=self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )

    def run(self):
        while True:
            self.ws.run_forever()

    def on_message(self, ws, message):
        print("thread trade")
        data = message.decode('utf-8')
        print(data)

    def on_error(self, ws, err):
        print(err)

    def on_close(self, ws, status_code, msg):
        print("closed!")

    def on_open(self, ws):
        print("connected!")
        self.ws.send(
            '[{"ticket":"test example"},{"type":"trade","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')


class SocketClient2(threading.Thread):
    def __init__(self):
        super().__init__()
        self.url = "wss://api.upbit.com/websocket/v1"
        self.ws = websocket.WebSocketApp(
            url=self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )

    def run(self):
        while True:
            self.ws.run_forever()

    def on_message(self, ws, message):
        print("thread ticker")
        data = message.decode('utf-8')
        print(data)

    def on_error(self, ws, err):
        print(err)

    def on_close(self, ws, status_code, msg):
        print("closed!")

    def on_open(self, ws):
        print("connected!")
        self.ws.send(
            '[{"ticket":"test example"},{"type":"ticker","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')


if __name__ == "__main__":
    # socket()
    lock = threading.Lock()
    socket1 = SocketClient1()
    socket2 = SocketClient2()

    socket1.start()
    socket2.start()


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

'''
{
    "type":"orderbook",
    "code":"KRW-SOL",
    "timestamp":1702797737116,
    "total_ask_size":4170.13027115,
    "total_bid_size":2871.05636465,
    "orderbook_units":[
        {"ask_price":100300.0,"bid_price":100200.0,"ask_size":35.12445126,"bid_size":53.26990314},
        {"ask_price":100350.0,"bid_price":100150.0,"ask_size":28.76919735,"bid_size":176.99218875},
        {"ask_price":100400.0,"bid_price":100100.0,"ask_size":95.80626746,"bid_size":522.74083965},
        {"ask_price":100450.0,"bid_price":100050.0,"ask_size":440.41746059,"bid_size":361.01212328},
        {"ask_price":100500.0,"bid_price":100000.0,"ask_size":111.31954012,"bid_size":819.40506862},
        {"ask_price":100550.0,"bid_price":99990.0,"ask_size":103.53450522,"bid_size":11.01169583},
        {"ask_price":100600.0,"bid_price":99980.0,"ask_size":299.03067474,"bid_size":17.70011443},
        {"ask_price":100650.0,"bid_price":99970.0,"ask_size":259.10329404,"bid_size":301.42703735},
        {"ask_price":100700.0,"bid_price":99960.0,"ask_size":402.50694852,"bid_size":2.60176169},
        {"ask_price":100750.0,"bid_price":99950.0,"ask_size":1393.08739033,"bid_size":52.66502042},
        {"ask_price":100800.0,"bid_price":99940.0,"ask_size":176.62652278,"bid_size":3.41976295},
        {"ask_price":100850.0,"bid_price":99930.0,"ask_size":114.45634043,"bid_size":0.84100848},
        {"ask_price":100900.0,"bid_price":99920.0,"ask_size":443.65883298,"bid_size":100.30024019},
        {"ask_price":100950.0,"bid_price":99910.0,"ask_size":2.05443537,"bid_size":301.39639923},
        {"ask_price":101000.0,"bid_price":99900.0,"ask_size":264.63440996,"bid_size":146.27320064}]
    ,"stream_type":"REALTIME"
}

{
    "type":"orderbook",
    "code":"KRW-BTC",
    "timestamp":1702797737203,
    "total_ask_size":2.85713835,
    "total_bid_size":1.32907028,
    "orderbook_units":[
        {"ask_price":5.7693E7,"bid_price":5.768E7,"ask_size":0.00399169,"bid_size":0.01551736},
        {"ask_price":5.7694E7,"bid_price":5.7672E7,"ask_size":0.99029119,"bid_size":0.1733},
        {"ask_price":5.7696E7,"bid_price":5.7669E7,"ask_size":0.15876201,"bid_size":0.53208092},
        {"ask_price":5.7697E7,"bid_price":5.7668E7,"ask_size":0.13604130,"bid_size":0.42520321},
        {"ask_price":5.7699E7,"bid_price":5.7667E7,"ask_size":0.11219886,"bid_size":0.00320597},
        {"ask_price":5.77E7,"bid_price":5.7666E7,"ask_size":0.05340882,"bid_size":0.00036794},
        {"ask_price":5.7705E7,"bid_price":5.7665E7,"ask_size":0.73526562,"bid_size":0.01854154},
        {"ask_price":5.772E7,"bid_price":5.7663E7,"ask_size":0.01732502,"bid_size":0.00018662},
        {"ask_price":5.7728E7,"bid_price":5.7662E7,"ask_size":0.07513893,"bid_size":0.00194161},
        {"ask_price":5.7729E7,"bid_price":5.766E7,"ask_size":0.02160161,"bid_size":0.00023043},
        {"ask_price":5.773E7,"bid_price":5.7658E7,"ask_size":0.20974257,"bid_size":0.10171361},
        {"ask_price":5.7731E7,"bid_price":5.7657E7,"ask_size":0.05005063,"bid_size":0.00135247},
        {"ask_price":5.7732E7,"bid_price":5.7656E7,"ask_size":0.21487693,"bid_size":0.00045798},
        {"ask_price":5.7733E7,"bid_price":5.7655E7,"ask_size":0.06885596,"bid_size":0.05431757},
        {"ask_price":5.7736E7,"bid_price":5.7654E7,"ask_size":0.00958721,"bid_size":0.00065305}],
    "stream_type":"REALTIME"
}
'''