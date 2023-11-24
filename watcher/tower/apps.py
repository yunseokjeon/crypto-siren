from django.apps import AppConfig
import threading
import websocket
import logging
import sys
import os

class TowerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tower'

    def ready(self):
        print("Hello")
        socket1 = SocketClient(0)
        socket2 = SocketClient(1)
        socket3 = SocketClient(2)
        socket1.start()
        socket2.start()
        socket3.start()

class SocketClient(threading.Thread):
    def __init__(self, category):
        super().__init__()
        self.url = "wss://api.upbit.com/websocket/v1"
        self.ws = websocket.WebSocketApp(
            url=self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.category = category
        self.step = 0

    def run(self):
        while True:
            self.ws.run_forever()

    def on_message(self, ws, message):
        data = message.decode('utf-8')
        if self.step < 100:
            print("----- ----- ----- ----- ----- ----- -----")
            print()
            if self.category == 0:
                print("ticker")
            elif self.category == 1:
                print("trade")
            elif self.category == 2:
                print("orderbook")
            print(data)
            print()
            print("----- ----- ----- ----- ----- ----- -----")
            self.step += 1

    def on_error(self, ws, err):
        print(err)

    def on_close(self, ws, status_code, msg):
        print("closed!")

    def on_open(self, ws):
        print("connected!")

        if self.category == 0:
            ws.send('[{"ticket":"siren0"},{"type":"ticker","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')
        elif self.category == 1:
            ws.send('[{"ticket":"siren1"},{"type":"trade","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')
        elif self.category == 2:
            ws.send('[{"ticket":"siren2"},{"type":"orderbook","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')





