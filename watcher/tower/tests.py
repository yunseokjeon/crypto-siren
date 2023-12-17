from django.test import TestCase
from .models import *
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

    def test_trade(self):
        raw = {"type": "trade",
               "code": "KRW-BTC",
               "timestamp": 1700365437515,
               "trade_date": "2023-11-19",
               "trade_time": "03:43:57",
               "trade_timestamp": 1700365437486,
               "trade_price": 49083000.0000,
               "trade_volume": 0.02430412,
               "ask_bid": "ASK",
               "prev_closing_price": 49165000.00000000,
               "change": "FALL",
               "change_price": 82000.00000000,
               "sequential_id": 1700365437486000,
               "stream_type": "REALTIME"
               }

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
        print(get_object_or_404(CryptoTrade, pk=trade.pk).id)

    def test_orderbook(self):
        raw1 = {
            "type": "orderbook",
            "code": "KRW-SOL",
            "timestamp": 1702797737116,
            "total_ask_size": 4170.13027115,
            "total_bid_size": 2871.05636465,
            "orderbook_units": [
                {"ask_price": 100300.0, "bid_price": 100200.0, "ask_size": 35.12445126, "bid_size": 53.26990314},
                {"ask_price": 100350.0, "bid_price": 100150.0, "ask_size": 28.76919735, "bid_size": 176.99218875},
                {"ask_price": 100400.0, "bid_price": 100100.0, "ask_size": 95.80626746, "bid_size": 522.74083965},
                {"ask_price": 100450.0, "bid_price": 100050.0, "ask_size": 440.41746059, "bid_size": 361.01212328},
                {"ask_price": 100500.0, "bid_price": 100000.0, "ask_size": 111.31954012, "bid_size": 819.40506862},
                {"ask_price": 100550.0, "bid_price": 99990.0, "ask_size": 103.53450522, "bid_size": 11.01169583},
                {"ask_price": 100600.0, "bid_price": 99980.0, "ask_size": 299.03067474, "bid_size": 17.70011443},
                {"ask_price": 100650.0, "bid_price": 99970.0, "ask_size": 259.10329404, "bid_size": 301.42703735},
                {"ask_price": 100700.0, "bid_price": 99960.0, "ask_size": 402.50694852, "bid_size": 2.60176169},
                {"ask_price": 100750.0, "bid_price": 99950.0, "ask_size": 1393.08739033, "bid_size": 52.66502042},
                {"ask_price": 100800.0, "bid_price": 99940.0, "ask_size": 176.62652278, "bid_size": 3.41976295},
                {"ask_price": 100850.0, "bid_price": 99930.0, "ask_size": 114.45634043, "bid_size": 0.84100848},
                {"ask_price": 100900.0, "bid_price": 99920.0, "ask_size": 443.65883298, "bid_size": 100.30024019},
                {"ask_price": 100950.0, "bid_price": 99910.0, "ask_size": 2.05443537, "bid_size": 301.39639923},
                {"ask_price": 101000.0, "bid_price": 99900.0, "ask_size": 264.63440996, "bid_size": 146.27320064}]
            , "stream_type": "REALTIME"
        }

        raw2 = {
            "type": "orderbook",
            "code": "KRW-BTC",
            "timestamp": 1702797737203,
            "total_ask_size": 2.85713835,
            "total_bid_size": 1.32907028,
            "orderbook_units": [
                {"ask_price": 5.7693E7, "bid_price": 5.768E7, "ask_size": 0.00399169, "bid_size": 0.01551736},
                {"ask_price": 5.7694E7, "bid_price": 5.7672E7, "ask_size": 0.99029119, "bid_size": 0.1733},
                {"ask_price": 5.7696E7, "bid_price": 5.7669E7, "ask_size": 0.15876201, "bid_size": 0.53208092},
                {"ask_price": 5.7697E7, "bid_price": 5.7668E7, "ask_size": 0.13604130, "bid_size": 0.42520321},
                {"ask_price": 5.7699E7, "bid_price": 5.7667E7, "ask_size": 0.11219886, "bid_size": 0.00320597},
                {"ask_price": 5.77E7, "bid_price": 5.7666E7, "ask_size": 0.05340882, "bid_size": 0.00036794},
                {"ask_price": 5.7705E7, "bid_price": 5.7665E7, "ask_size": 0.73526562, "bid_size": 0.01854154},
                {"ask_price": 5.772E7, "bid_price": 5.7663E7, "ask_size": 0.01732502, "bid_size": 0.00018662},
                {"ask_price": 5.7728E7, "bid_price": 5.7662E7, "ask_size": 0.07513893, "bid_size": 0.00194161},
                {"ask_price": 5.7729E7, "bid_price": 5.766E7, "ask_size": 0.02160161, "bid_size": 0.00023043},
                {"ask_price": 5.773E7, "bid_price": 5.7658E7, "ask_size": 0.20974257, "bid_size": 0.10171361},
                {"ask_price": 5.7731E7, "bid_price": 5.7657E7, "ask_size": 0.05005063, "bid_size": 0.00135247},
                {"ask_price": 5.7732E7, "bid_price": 5.7656E7, "ask_size": 0.21487693, "bid_size": 0.00045798},
                {"ask_price": 5.7733E7, "bid_price": 5.7655E7, "ask_size": 0.06885596, "bid_size": 0.05431757},
                {"ask_price": 5.7736E7, "bid_price": 5.7654E7, "ask_size": 0.00958721, "bid_size": 0.00065305}],
            "stream_type": "REALTIME"
        }

        book_main = CryptoOrderbookMain()
        book_main.exchange = "Upbit"
        book_main.code = raw2["code"]
        book_main.server_timestamp = raw2["timestamp"]
        book_main.total_ask_size = raw2["total_ask_size"]
        book_main.total_bid_size = raw2["total_bid_size"]
        book_main.save()

        fk = get_object_or_404(CryptoOrderbookMain, pk=book_main.pk).id

        for unit in raw2["orderbook_units"]:
            book_sub = CryptoOrderbookSub()
            book_sub.main_key = fk
            book_sub.ask_price = unit["ask_price"]
            book_sub.bid_price = unit["bid_price"]
            book_sub.ask_size = unit["ask_size"]
            book_sub.bid_size = unit["bid_size"]
            book_sub.save()

            print(get_object_or_404(CryptoOrderbookSub, pk=book_sub.pk).id)



