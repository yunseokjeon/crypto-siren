from django.apps import AppConfig
import threading, time
import websocket
from jproperties import Properties
import uuid
import jwt
import configparser
from django.conf import settings
import platform
from datetime import datetime
import pytz
from django.shortcuts import get_object_or_404
import json

BASE_DIR = settings.BASE_DIR
config_path = ''

if platform.system() == 'Windows' :
    config_path = f"%s\config\config.ini" % BASE_DIR
else:
    config_path = f"%s/config/config.ini" % BASE_DIR

config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')
upbit_key = config.get('Upbit', 'upbit_key')
upbit_secret = config.get('Upbit', 'upbit_secret')

payload = {
    'access_key': upbit_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, upbit_secret)
authorization_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorization_token}

class TowerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tower'

    def ready(self):
        print("Hello")
        socket = SocketClient()
        socket.start()

class SocketClient(threading.Thread):
    def __init__(self):
        super().__init__()
        self.url = "wss://api.upbit.com/websocket/v1"


        self.ws = websocket.WebSocketApp(
            url=self.url,
            header=headers,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )

        self.step = 0

    def run(self):
        while True:
            if not self.ws.sock:
                self.ws.run_forever()

    def on_message(self, ws, message):
        data = message.decode('utf-8')
        self.process(data)

    def on_error(self, ws, err):
        print('on_error')
        print(err)

        time.sleep(5)
        self.ws.sock = None
        self.ws = websocket.WebSocketApp(
            url=self.url,
            header=headers,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.ws.run_forever()

    def on_close(self, ws, status_code, msg):
        print("closed!")

    def on_open(self, ws):
        print("connected!")
        ws.send('[{"ticket":"siren1"}, {"type":"ticker","codes":["KRW-BTC", "KRW-SOL"]}, {"type":"trade","codes":["KRW-BTC", "KRW-SOL"]}, {"type":"orderbook","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')

    def process(self, data):

        from .models import CryptoTicker, CryptoTrade, CryptoOrderbookMain, CryptoOrderbookSub

        raw = json.loads(data)

        if raw["type"] == "ticker" and raw["stream_type"] == "REALTIME":
            ticker = CryptoTicker()
            ticker.exchange = "Upbit"
            ticker.code = raw["code"]
            ticker.opening_price = raw["opening_price"]
            ticker.high_price = raw["high_price"]
            ticker.low_price = raw["low_price"]
            ticker.trade_price = raw["trade_price"]
            ticker.prev_closing_price = raw["prev_closing_price"]
            ticker.acc_trade_price = raw["acc_trade_price"]
            ticker.change = raw["change"]
            ticker.change_price = raw["change_price"]
            ticker.signed_change_price = raw["signed_change_price"]
            ticker.change_rate = raw["change_rate"]
            ticker.signed_change_rate = raw["signed_change_rate"]
            ticker.ask_bid = raw["ask_bid"]
            ticker.trade_volume = raw["trade_volume"]
            ticker.acc_trade_volume = raw["acc_trade_volume"]

            date = raw["trade_date"]
            time = raw["trade_time"]
            ticker.trade_date = datetime(int(date[0:4]), int(date[4:6]), int(date[6:]), int(time[0:2]), int(time[2:4]),
                                         int(time[4:]), tzinfo=pytz.UTC)

            ticker.trade_timestamp = raw["trade_timestamp"]
            ticker.acc_ask_volume = raw["acc_ask_volume"]
            ticker.acc_bid_volume = raw["acc_bid_volume"]
            ticker.server_timestamp = raw["timestamp"]
            ticker.acc_trade_price_24h = raw["acc_trade_price_24h"]
            ticker.acc_trade_volume_24h = raw["acc_trade_volume_24h"]

            # ticker.save()

        elif raw["type"] == "trade" and raw["stream_type"] == "REALTIME":
            trade = CryptoTrade()
            trade.exchange = "Upbit"
            trade.code = raw["code"]
            trade.server_timestamp = raw["timestamp"]

            date = raw["trade_date"]
            time = raw["trade_time"]
            trade.trade_date = datetime(int(date[0:4]), int(date[5:7]), int(date[8:]), int(time[0:2]), int(time[3:5]),
                                        int(time[6:]), tzinfo=pytz.UTC)

            trade.trade_timestamp = raw["trade_timestamp"]
            trade.trade_price = raw["trade_price"]
            trade.trade_volume = raw["trade_volume"]
            trade.ask_bid = raw["ask_bid"]
            trade.change = raw["change"]
            trade.change_price = raw["change_price"]
            trade.sequential_id = raw["sequential_id"]

            trade.save()

        elif raw["type"] == "orderbook" and raw["stream_type"] == "REALTIME":
            book_main = CryptoOrderbookMain()
            book_main.exchange = "Upbit"
            book_main.code = raw["code"]
            book_main.server_timestamp = raw["timestamp"]
            book_main.total_ask_size = raw["total_ask_size"]
            book_main.total_bid_size = raw["total_bid_size"]
            book_main.save()
            fk = get_object_or_404(CryptoOrderbookMain, pk=book_main.pk).id

            for unit in raw["orderbook_units"]:
                book_sub = CryptoOrderbookSub()
                book_sub.main_key = fk
                book_sub.ask_price = unit["ask_price"]
                book_sub.bid_price = unit["bid_price"]
                book_sub.ask_size = unit["ask_size"]
                book_sub.bid_size = unit["bid_size"]
                book_sub.save()



