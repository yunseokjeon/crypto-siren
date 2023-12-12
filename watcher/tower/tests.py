from django.test import TestCase
from .models import CryptoTicker
from datetime import datetime
import pytz
from django.shortcuts import get_object_or_404

# python manage.py test
# Create your tests here.

class TestModule(TestCase):

    def setUp(self):
        pass

    def test_ticker(self):

        raw = {"type": "ticker",
               "code": "KRW-BTC",
               "opening_price": 49190000.0000,
               "high_price": 49200000.0000,
               "low_price": 49023000.0000,
               "trade_price": 49053000.0000,
               "prev_closing_price": 49165000.00000000,
               "acc_trade_price": 12749660933.205850000000,
               "change": "FALL",
               "change_price": 112000.00000000,
               "signed_change_price": -112000.00000000,
               "change_rate": 0.0022780433,
               "signed_change_rate": -0.0022780433,
               "ask_bid": "ASK",
               "trade_volume": 0.03600000,
               "acc_trade_volume": 259.64633542,
               "trade_date": "20231119",
               "trade_time": "033048",
               "trade_timestamp": 1700364648886,
               "acc_ask_volume": 157.22379616,
               "acc_bid_volume": 102.42253926,
               "highest_52_week_price": 50652000.0000,
               "highest_52_week_date": "2023-11-16",
               "lowest_52_week_price": 20700000.00000000,
               "lowest_52_week_date": "2022-12-30",
               "market_state": "ACTIVE",
               "is_trading_suspended": "false",
               "delisting_date": "null",
               "market_warning": "NONE",
               "timestamp": 1700364648910,
               "acc_trade_price_24h": 85934950517.43824000,
               "acc_trade_volume_24h": 1749.53713304,
               "stream_type": "REALTIME"
               }

        ticker = CryptoTicker()
        ticker.exchange = 'Upbit'
        ticker.code = raw['code']
        ticker.opening_price = raw['opening_price']
        ticker.high_price = raw['high_price']
        ticker.low_price = raw['low_price']
        ticker.trade_price = raw['trade_price']
        ticker.prev_closing_price = raw['prev_closing_price']
        ticker.acc_trade_price = raw['acc_trade_price']
        ticker.change = raw['change']
        ticker.change_price = raw['change_price']
        ticker.signed_change_price = raw['signed_change_price']
        ticker.change_rate = raw['change_rate']
        ticker.signed_change_rate = raw['signed_change_rate']
        ticker.ask_bid = raw['ask_bid']
        ticker.trade_volume = raw['trade_volume']
        ticker.acc_trade_volume = raw['acc_trade_volume']

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

        ticker.save()
        print(get_object_or_404(CryptoTicker, pk=ticker.pk).id)

        self.assertEqual(1, 1)
