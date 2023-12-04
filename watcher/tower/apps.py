from django.apps import AppConfig
import threading
import websocket
from jproperties import Properties
import uuid
import jwt
import configparser
from django.conf import settings
import platform

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
            self.ws.run_forever()

    def on_message(self, ws, message):
        data = message.decode('utf-8')
        if self.step < 0:
            print("----- ----- ----- ----- ----- ----- -----")
            print()
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
        ws.send('[{"ticket":"siren1"}, {"type":"ticker","codes":["KRW-BTC", "KRW-SOL"]}, {"type":"trade","codes":["KRW-BTC", "KRW-SOL"]}, {"type":"orderbook","codes":["KRW-BTC", "KRW-SOL"]}, {"format": "DEFAULT"}]')
