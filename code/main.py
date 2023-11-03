import requests
from jproperties import Properties

# https://pypi.org/project/python-binance/
from binance.client import Client

# https://github.com/binance/binance-connector-python
from binance.spot import Spot

# https://github.com/binance/binance-futures-connector-python
from binance.cm_futures import CMFutures

import ccxt
import time
import pandas as pd

# application.properties
configs = Properties()
with open('./resource/application.properties', 'rb') as config_file:
    configs.load(config_file)

binanceKey = configs.get('BINANCE_KEY').data
binanceSecret = configs.get('BINANCE_SECRET').data

client = Client(binanceKey, binanceSecret)

# Get Market Depth
depth = client.get_order_book(symbol='BNBBTC')
# print(depth)
'''
{'lastUpdateId': 3167800612, 
    'bids': [['0.00664200', '10.46500000'], ['0.00664100', '10.98100000'], ['0.00664000', '14.50500000'], ['0.00663900', '6.88500000'], ['0.00663800', '0.52200000'], ['0.00663700', '2.70100000'], ['0.00663600', '30.36200000'], ['0.00663500', '82.78600000'], ['0.00663400', '16.82800000'], ['0.00663300', '9.71300000'], ['0.00663200', '0.93600000'], ['0.00663100', '0.55400000'], ['0.00663000', '0.55400000'], ['0.00662900', '103.34000000'], ['0.00662800', '0.55400000'], ['0.00662700', '0.55400000'], ['0.00662600', '1.65700000'], ['0.00662500', '15.10000000'], ['0.00662400', '0.57200000'], ['0.00662300', '196.63800000'], ['0.00662200', '64.71600000'], ['0.00662100', '0.55400000'], ['0.00662000', '0.57800000'], ['0.00661900', '0.55400000'], ['0.00661800', '0.57100000'], ['0.00661700', '0.84200000'], ['0.00661600', '0.62200000'], ['0.00661500', '454.06900000'], ['0.00661400', '9.87100000'], ['0.00661300', '120.39000000'], ['0.00661200', '0.55400000'], ['0.00661100', '0.58700000'], ['0.00661000', '0.57600000'], ['0.00660900', '0.69400000'], ['0.00660800', '12.58500000'], ['0.00660700', '2.66500000'], ['0.00660600', '0.77700000'], ['0.00660500', '0.78700000'], ['0.00660400', '0.63900000'], ['0.00660300', '80.63800000'], ['0.00660200', '0.92100000'], ['0.00660100', '0.59000000'], ['0.00660000', '16.11900000'], ['0.00659900', '0.58400000'], ['0.00659800', '8.82900000'], ['0.00659700', '0.63700000'], ['0.00659600', '0.84200000'], ['0.00659500', '1.24700000'], ['0.00659400', '0.64400000'], ['0.00659300', '533.97100000'], ['0.00659200', '1.54400000'], ['0.00659100', '0.55400000'], ['0.00659000', '1.43700000'], ['0.00658900', '0.55400000'], ['0.00658800', '0.64100000'], ['0.00658700', '0.57000000'], ['0.00658600', '0.55400000'], ['0.00658500', '0.55400000'], ['0.00658400', '12.59200000'], ['0.00658300', '1.01100000'], ['0.00658200', '1.50700000'], ['0.00658100', '0.66500000'], ['0.00658000', '1.78000000'], ['0.00657900', '1.87800000'], ['0.00657800', '0.59000000'], ['0.00657700', '41.01800000'], ['0.00657600', '0.74400000'], ['0.00657500', '3.25600000'], ['0.00657400', '0.64400000'], ['0.00657300', '0.57200000'], ['0.00657200', '0.55400000'], ['0.00657100', '26.31700000'], ['0.00657000', '1.43500000'], ['0.00656900', '0.57100000'], ['0.00656800', '0.71200000'], ['0.00656700', '0.04900000'], ['0.00656600', '2.65700000'], ['0.00656500', '0.35100000'], ['0.00656400', '0.08200000'], ['0.00656300', '44.05000000'], ['0.00656200', '1.18000000'], ['0.00656100', '12.44200000'], ['0.00656000', '0.78400000'], ['0.00655900', '0.02200000'], ['0.00655800', '0.57000000'], ['0.00655700', '1.21800000'], ['0.00655600', '0.51700000'], ['0.00655500', '1.08600000'], ['0.00655400', '43.69900000'], ['0.00655300', '0.10000000'], ['0.00655200', '2.19000000'], ['0.00655100', '0.15400000'], ['0.00655000', '0.13900000'], ['0.00654900', '6.83800000'], ['0.00654800', '6.82800000'], ['0.00654600', '8.34800000'], ['0.00654500', '0.01600000'], ['0.00654400', '0.03800000'], ['0.00654300', '2.81000000'], ['0.00654200', '0.22200000']], 
    'asks': [['0.00664300', '9.18100000'], ['0.00664400', '16.93600000'], ['0.00664500', '34.60700000'], ['0.00664600', '16.10800000'], ['0.00664700', '10.09300000'], ['0.00664800', '16.24600000'], ['0.00664900', '18.94300000'], ['0.00665000', '27.18000000'], ['0.00665100', '82.84200000'], ['0.00665200', '2.74800000'], ['0.00665300', '0.75300000'], ['0.00665400', '8.43700000'], ['0.00665500', '15.89100000'], ['0.00665600', '90.58200000'], ['0.00665700', '13.01200000'], ['0.00665800', '2.87100000'], ['0.00665900', '9.18400000'], ['0.00666000', '0.61500000'], ['0.00666100', '0.58600000'], ['0.00666200', '10.61100000'], ['0.00666300', '0.60900000'], ['0.00666400', '196.21500000'], ['0.00666500', '0.55400000'], ['0.00666600', '2.42400000'], ['0.00666700', '0.67200000'], ['0.00666800', '0.57000000'], ['0.00666900', '8.39100000'], ['0.00667000', '0.67100000'], ['0.00667100', '2.65300000'], ['0.00667200', '0.57600000'], ['0.00667300', '0.55400000'], ['0.00667400', '120.40700000'], ['0.00667500', '25.55400000'], ['0.00667600', '0.63600000'], ['0.00667700', '1.24400000'], ['0.00667800', '12.53300000'], ['0.00667900', '0.60900000'], ['0.00668000', '2.96500000'], ['0.00668100', '0.88600000'], ['0.00668200', '0.64600000'], ['0.00668300', '0.80400000'], ['0.00668400', '173.96500000'], ['0.00668500', '0.72400000'], ['0.00668600', '4.89800000'], ['0.00668700', '0.55400000'], ['0.00668800', '0.60500000'], ['0.00668900', '0.51500000'], ['0.00669000', '0.55400000'], ['0.00669100', '1.58100000'], ['0.00669200', '0.59600000'], ['0.00669300', '2.16400000'], ['0.00669400', '0.59000000'], ['0.00669500', '0.62600000'], ['0.00669600', '0.55400000'], ['0.00669700', '0.60500000'], ['0.00669800', '0.55400000'], ['0.00669900', '0.57000000'], ['0.00670000', '14.87000000'], ['0.00670100', '0.96900000'], ['0.00670200', '15.89100000'], ['0.00670300', '2.61900000'], ['0.00670400', '0.67100000'], ['0.00670500', '0.57200000'], ['0.00670600', '1.51900000'], ['0.00670700', '0.90100000'], ['0.00670800', '0.62000000'], ['0.00670900', '5.14200000'], ['0.00671000', '0.92500000'], ['0.00671100', '2.18400000'], ['0.00671200', '0.61100000'], ['0.00671300', '1.43300000'], ['0.00671400', '0.63200000'], ['0.00671500', '2.20100000'], ['0.00671600', '0.59000000'], ['0.00671700', '1.79600000'], ['0.00671800', '1.07000000'], ['0.00671900', '1.71800000'], ['0.00672000', '0.57600000'], ['0.00672100', '0.78400000'], ['0.00672200', '0.05800000'], ['0.00672300', '41.26800000'], ['0.00672400', '2.91500000'], ['0.00672600', '17.06500000'], ['0.00672700', '0.31400000'], ['0.00672800', '0.63600000'], ['0.00672900', '0.50000000'], ['0.00673000', '0.57600000'], ['0.00673100', '0.07000000'], ['0.00673200', '3.55100000'], ['0.00673300', '200.98300000'], ['0.00673400', '0.06600000'], ['0.00673500', '2.68800000'], ['0.00673600', '0.69300000'], ['0.00673700', '0.03300000'], ['0.00673800', '5.35800000'], ['0.00673900', '0.02900000'], ['0.00674000', '0.43400000'], ['0.00674100', '0.02400000'], ['0.00674200', '1.14300000'], ['0.00674300', '0.04300000']]
    }
'''

# Get Recent Trades
trades = client.get_recent_trades(symbol='BNBBTC')
# print(trades)
'''
[   {'id': 228400753, 'price': '0.00663800', 'qty': '0.67300000', 'quoteQty': '0.00446737', 'time': 1699010000661, 'isBuyerMaker': True, 'isBestMatch': True}, 
    {'id': 228400754, 'price': '0.00663900', 'qty': '0.55400000', 'quoteQty': '0.00367800', 'time': 1699010004830, 'isBuyerMaker': False, 'isBestMatch': True}, 
    생략    
]
'''

# Get Historical Trades
trades = client.get_historical_trades(symbol='BNBBTC')
# print(trades)

# Get Aggregate Trades
trades = client.get_aggregate_trades(symbol='BNBBTC')
# print(trades)
'''
[   {'a': 163599434, 'p': '0.00663900', 'q': '0.01700000', 'f': 228400780, 'l': 228400780, 'T': 1699010103795, 'm': False, 'M': True}, 
    {'a': 163599435, 'p': '0.00663900', 'q': '0.01900000', 'f': 228400781, 'l': 228400781, 'T': 1699010105549, 'm': False, 'M': True}, 
    생략 
]
'''

# Get Kline/Candlesticks
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
# print(candles)

'''
[
    [1698114600000, '0.00672900', '0.00683800', '0.00671000', '0.00681700', '2133.60300000', 1698116399999, '14.46429642', 2248, '1062.50700000', '7.20316556', '0'], 
    [1698116400000, '0.00681500', '0.00682500', '0.00673400', '0.00674300', '1857.04600000', 1698118199999, '12.57860002', 1694, '983.01100000', '6.65821127', '0'], 
    생략
]
'''

# Get Orderbook Tickers
tickers = client.get_orderbook_tickers()

# Binance
client = Spot(api_key=binanceKey, api_secret=binanceSecret)
# print(client.time())

# https://github.com/binance/binance-connector-python/blob/master/examples/spot/market/book_ticker.py
# print(client.book_ticker("BTCUSDT"))
# print(client.book_ticker(symbols=["BTCUSDT", "BNBUSDT"]))

# https://github.com/binance/binance-connector-python/blob/master/examples/spot/market/depth.py
# print(client.depth("BTCUSDT", limit=10))

'''
{'lastUpdateId': 40064412888, 
    'bids': [['34348.03000000', '2.03776000'], ['34347.93000000', '0.00070000'], ['34347.61000000', '0.00030000'], ['34347.49000000', '0.00312000'], ['34347.43000000', '0.00134000'], ['34347.06000000', '0.00060000'], ['34347.05000000', '0.00070000'], ['34346.82000000', '0.02923000'], ['34346.68000000', '0.00134000'], ['34346.61000000', '0.00070000']], 
    'asks': [['34348.04000000', '6.33048000'], ['34348.12000000', '0.29109000'], ['34348.20000000', '0.02923000'], ['34348.30000000', '0.06048000'], ['34348.55000000', '0.29109000'], ['34348.81000000', '0.00070000'], ['34348.89000000', '0.02923000'], ['34348.92000000', '0.07600000'], ['34348.93000000', '0.00134000'], ['34349.25000000', '0.00070000']]
    }
'''

# https://github.com/binance/binance-connector-python/blob/master/examples/spot/market/exchange_info.py
# print(client.exchange_info(permissions=["MARGIN"]))

# https://github.com/binance/binance-connector-python/blob/master/examples/spot/market/historical_trades.py
# print(client.historical_trades("BTCUSDT"))
# print(client.trades("BTCUSDT"))

'''
[
    {'id': 3267406836, 'price': '34369.94000000', 'qty': '0.04854000', 'quoteQty': '1668.31688760', 'time': 1699017959003, 'isBuyerMaker': True, 'isBestMatch': True}, 
    {'id': 3267406837, 'price': '34369.94000000', 'qty': '0.00407000', 'quoteQty': '139.88565580', 'time': 1699017959003, 'isBuyerMaker': True, 'isBestMatch': True}, 
]
'''

# https://wikidocs.net/129746

ccxtBinance = ccxt.binance(config={
    'apiKey': binanceKey,
    'secret': binanceSecret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

btc = ccxtBinance.fetch_ticker("BTC/USDT")
# print(btc)

'''
{   'symbol': 'BTC/USDT:USDT', 
    'timestamp': 1699019732061, 
    'datetime': '2023-11-03T13:55:32.061Z', 
    'high': 35099.0, 
    'low': 34123.0, 
    'bid': None, 
    'bidVolume': None, 
    'ask': None, 
    'askVolume': None, 
    'vwap': 34584.59, 
    'open': 34978.0, 
    'close': 34513.6, 
    'last': 34513.6, 
    'previousClose': None, 
    'change': -464.4, 
    'percentage': -1.328, 
    'average': 34745.8, 
    'baseVolume': 348955.874, 
    'quoteVolume': 12068496182.89, 
    'info': {'symbol': 'BTCUSDT', 'priceChange': '-464.40', 'priceChangePercent': '-1.328', 'weightedAvgPrice': '34584.59', 'lastPrice': '34513.60', 'lastQty': '0.145', 'openPrice': '34978.00', 'highPrice': '35099.00', 'lowPrice': '34123.00', 'volume': '348955.874', 'quoteVolume': '12068496182.89', 'openTime': '1698933300000', 'closeTime': '1699019732061', 'firstId': '4252198713', 'lastId': '4255774069', 'count': '3575326'}}
'''

btc = ccxtBinance.fetch_ohlcv(
    symbol="BTC/USDT",
    timeframe='1m',
    since=None,
    limit=10)

df = pd.DataFrame(btc, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime', inplace=True)
# print(df)

# https://github.com/ccxt/ccxt/wiki/Manual#order-book
btc = ccxtBinance.fetch_order_book("BTC/USDT")
# print(btc)

'''
{   'symbol': 'BTC/USDT', 
    'bids': [[34539.0, 4.561], [34538.9, 0.027], [34538.7, 0.053], [34538.6, 0.012], [34538.5, 0.021], [34538.4, 0.001], [34538.3, 0.058], [34538.1, 0.006], [34538.0, 0.013], [34537.9, 0.006], [34537.8, 0.003], [34537.5, 0.017], [34537.2, 0.012], [34537.0, 0.016], [34536.9, 0.004], [34536.8, 0.262], [34536.7, 0.031], [34536.5, 0.013], [34536.4, 0.003], [34536.1, 1.119], [34536.0, 0.106], [34535.9, 0.011], [34535.7, 2.955], [34535.6, 0.008], [34535.5, 0.02], [34535.4, 0.101], [34535.3, 0.009], [34535.2, 0.034], [34535.1, 0.274], [34535.0, 0.538], [34534.9, 0.06], [34534.8, 0.015], [34534.6, 0.003], [34534.5, 0.091], [34534.4, 0.538], [34534.3, 1.491], [34534.1, 0.32], [34534.0, 0.448], [34533.9, 0.081], [34533.8, 0.927], [34533.7, 0.463], [34533.6, 0.64], [34533.5, 0.015], [34533.3, 0.172], [34533.2, 0.006], [34533.1, 0.003], [34533.0, 1.11], [34532.9, 0.003], [34532.8, 0.058], [34532.7, 0.313], [34532.6, 0.348], [34532.5, 0.009], [34532.4, 0.012], [34532.3, 0.087], [34532.2, 0.16], [34532.1, 1.232], [34532.0, 0.075], [34531.9, 0.589], [34531.8, 0.211], [34531.7, 0.177], [34531.6, 1.851], [34531.5, 3.4], [34531.4, 0.001], [34531.2, 0.076], [34531.1, 2.394], [34531.0, 6.064], [34530.9, 0.003], [34530.8, 0.341], [34530.5, 0.003], [34530.4, 0.023], [34530.3, 1.094], [34530.2, 0.012], [34530.1, 0.481], [34530.0, 0.928], [34529.9, 1.365], [34529.8, 0.599], [34529.7, 0.023], [34529.6, 0.004], [34529.5, 3.709], [34529.4, 0.071], [34529.3, 0.292], [34529.2, 1.244], [34529.1, 0.066], [34529.0, 0.076], [34528.9, 0.245], [34528.8, 0.097], [34528.7, 0.053], [34528.6, 7.724], [34528.5, 1.652], [34528.4, 1.389], [34528.3, 1.574], [34528.2, 1.834], [34528.1, 0.758], [34528.0, 6.027], [34527.9, 1.614], [34527.8, 0.098], [34527.7, 1.734], [34527.6, 1.019], [34527.5, 0.045], [34527.4, 0.177], [34527.3, 0.006], [34527.2, 1.883], [34527.1, 2.104], [34527.0, 0.516], [34526.9, 0.666], [34526.8, 0.571], [34526.7, 2.138], [34526.6, 0.171], [34526.5, 0.237], [34526.4, 0.056], [34526.3, 0.073], [34526.2, 0.237], [34526.1, 0.706], [34526.0, 1.003], [34525.9, 0.157], [34525.8, 1.677], [34525.7, 2.5], [34525.6, 0.082], [34525.5, 1.603], [34525.4, 0.712], [34525.3, 0.065], [34525.2, 2.662], [34525.1, 3.064], [34525.0, 0.761], [34524.9, 0.498], [34524.8, 0.377], [34524.7, 0.177], [34524.6, 1.797], [34524.5, 4.653], [34524.4, 3.405], [34524.3, 1.502], [34524.2, 0.043], [34524.1, 1.4], [34524.0, 1.47], [34523.9, 1.023], [34523.8, 0.094], [34523.7, 0.341], [34523.6, 0.645], [34523.5, 0.269], [34523.4, 1.721], [34523.3, 0.151], [34523.2, 1.006], [34523.1, 0.16], [34523.0, 0.508], [34522.9, 0.077], [34522.8, 0.871], [34522.7, 0.166], [34522.6, 0.018], [34522.5, 2.261], [34522.4, 0.253], [34522.3, 1.256], [34522.2, 0.935], [34522.1, 0.05], [34522.0, 0.995], [34521.9, 0.178], [34521.8, 0.012], [34521.7, 0.302], [34521.6, 0.859], [34521.5, 1.688], [34521.4, 0.049], [34521.3, 0.106], [34521.2, 1.697], [34521.1, 0.491], [34521.0, 1.988], [34520.9, 0.723], [34520.8, 0.073], [34520.7, 1.529], [34520.6, 0.11], [34520.5, 4.485], [34520.4, 0.161], [34520.3, 0.004], [34520.2, 2.452], [34520.0, 4.916], [34519.9, 0.071], [34519.8, 1.454], [34519.7, 0.853], [34519.6, 0.124], [34519.5, 0.116], [34519.4, 0.168], [34519.2, 0.131], [34519.1, 1.799], [34519.0, 6.034], [34518.9, 0.298], [34518.8, 0.239], [34518.7, 0.419], [34518.6, 0.109], [34518.5, 1.327], [34518.4, 0.298], [34518.3, 2.568], [34518.2, 0.197], [34518.0, 1.505], [34517.9, 0.738], [34517.8, 7.075], [34517.7, 0.109], [34517.6, 1.443], [34517.5, 0.607], [34517.4, 0.332], [34517.3, 0.17], [34517.2, 0.865], [34517.1, 4.755], [34517.0, 0.499], [34516.9, 0.421], [34516.8, 2.659], [34516.7, 0.008], [34516.6, 7.742], [34516.5, 0.068], [34516.3, 0.064], [34516.2, 0.101], [34516.1, 1.231], [34516.0, 1.096], [34515.7, 0.326], [34515.6, 0.288], [34515.5, 0.013], [34515.4, 0.157], [34515.3, 0.06], [34515.2, 0.72], [34515.1, 0.039], [34515.0, 4.656], [34514.9, 2.409], [34514.8, 1.904], [34514.7, 0.165], [34514.6, 0.018], [34514.5, 0.065], [34514.4, 0.033], [34514.3, 2.132], [34514.2, 4.741], [34514.1, 2.451], [34514.0, 2.808], [34513.9, 0.176], [34513.8, 0.015], [34513.6, 2.613], [34513.5, 0.113], [34513.4, 4.653], [34513.3, 0.161], [34513.2, 0.073], [34513.1, 0.143], [34513.0, 0.004], [34512.9, 1.639], [34512.8, 6.004], [34512.7, 8.562], [34512.6, 0.653], [34512.5, 6.309], [34512.4, 0.006], [34512.3, 0.379], [34512.2, 0.072], [34512.1, 0.34], [34512.0, 1.262], [34511.9, 2.069], [34511.8, 1.02], [34511.7, 0.036], [34511.6, 0.002], [34511.5, 0.119], [34511.4, 0.597], [34511.3, 0.104], [34511.2, 1.728], [34511.1, 3.004], [34511.0, 0.019], [34510.8, 3.159], [34510.7, 0.224], [34510.6, 1.119], [34510.5, 0.007], [34510.4, 0.4], [34510.3, 0.074], [34510.2, 0.003], [34510.1, 0.641], [34510.0, 3.089], [34509.9, 0.01], [34509.8, 0.005], [34509.7, 0.003], [34509.6, 0.548], [34509.5, 2.259], [34509.4, 0.477], [34509.3, 0.09], [34509.2, 0.074], [34509.1, 0.1], [34509.0, 0.003], [34508.9, 0.104], [34508.8, 4.225], [34508.7, 5.032], [34508.5, 0.103], [34508.3, 0.032], [34508.1, 2.477], [34508.0, 0.929], [34507.9, 3.122], [34507.8, 0.81], [34507.7, 3.0], [34507.6, 7.219], [34507.5, 0.023], [34507.4, 0.003], [34507.3, 0.003], [34507.2, 0.031], [34507.1, 0.1], [34507.0, 0.031], [34506.9, 1.448], [34506.8, 0.498], [34506.6, 1.004], [34506.5, 0.72], [34506.4, 0.003], [34506.3, 3.002], [34506.1, 0.015], [34506.0, 1.888], [34505.9, 0.003], [34505.8, 4.457], [34505.7, 2.012], [34505.6, 1.072], [34505.5, 1.037], [34505.4, 0.007], [34505.3, 0.011], [34505.2, 0.058], [34505.1, 0.012], [34505.0, 5.104], [34504.9, 3.024], [34504.8, 0.024], [34504.7, 0.009], [34504.5, 0.124], [34504.4, 0.175], [34504.2, 0.016], [34504.1, 0.019], [34504.0, 4.153], [34503.9, 0.015], [34503.8, 8.553], [34503.6, 0.02], [34503.5, 0.416], [34503.4, 0.399], [34503.3, 0.011], [34503.2, 0.007], [34503.1, 5.165], [34503.0, 14.378], [34502.9, 5.207], [34502.8, 0.005], [34502.7, 0.008], [34502.6, 0.058], [34502.5, 0.003], [34502.4, 0.01], [34502.3, 0.001], [34502.2, 0.657], [34502.1, 0.009], [34502.0, 0.419], [34501.9, 2.533], [34501.8, 0.037], [34501.7, 0.73], [34501.6, 0.217], [34501.5, 5.206], [34501.4, 0.008], [34501.3, 2.854], [34501.2, 0.982], [34501.1, 0.035], [34501.0, 0.915], [34500.9, 0.164], [34500.8, 0.156], [34500.7, 3.0], [34500.6, 0.059], [34500.5, 8.259], [34500.4, 0.412], [34500.2, 0.003], [34500.0, 25.902], [34499.9, 0.022], [34499.8, 1.071], [34499.7, 1.961], [34499.5, 0.106], [34499.4, 0.036], [34499.3, 0.135], [34499.2, 0.008], [34499.1, 1.372], [34499.0, 0.044], [34498.9, 1.336], [34498.6, 0.015], [34498.5, 0.058], [34498.4, 1.738], [34498.2, 0.004], [34498.1, 0.004], [34498.0, 0.032], [34497.9, 0.027], [34497.8, 0.318], [34497.7, 6.001], [34497.6, 3.001], [34497.5, 0.032], [34497.3, 2.692], [34497.2, 3.089], [34497.1, 3.0], [34497.0, 0.021], [34496.9, 0.503], [34496.8, 2.443], [34496.7, 0.004], [34496.6, 0.243], [34496.5, 2.287], [34496.4, 0.034], [34496.3, 1.177], [34496.2, 4.62], [34496.1, 0.001], [34496.0, 3.287], [34495.9, 0.623], [34495.8, 0.04], [34495.7, 1.509], [34495.5, 0.053], [34495.4, 0.193], [34495.2, 0.002], [34495.1, 0.01], [34495.0, 0.435], [34494.9, 0.011], [34494.8, 0.058], [34494.7, 0.004], [34494.5, 0.083], [34494.4, 0.019], [34494.3, 0.145], [34494.2, 0.9], [34494.1, 0.114], [34494.0, 0.039], [34493.9, 0.537], [34493.8, 0.045], [34493.7, 1.407], [34493.6, 0.097], [34493.5, 0.003], [34493.4, 0.012], [34493.3, 0.008], [34493.2, 3.899], [34493.1, 0.05], [34493.0, 0.008], [34492.9, 0.003], [34492.8, 0.104], [34492.7, 0.064], [34492.6, 1.758], [34492.5, 0.013], [34492.4, 0.142], [34492.3, 6.459], [34492.2, 0.353], [34492.1, 0.496], [34492.0, 0.985], [34491.9, 0.01], [34491.8, 1.911], [34491.7, 18.243], [34491.6, 3.472], [34491.5, 0.003], [34491.4, 0.001], [34491.3, 0.004], [34491.2, 0.066], [34491.1, 7.724], [34491.0, 0.922], [34490.9, 0.004], [34490.7, 0.174], [34490.6, 1.825], [34490.5, 0.346], [34490.4, 0.499], [34490.3, 1.449], [34490.1, 0.009], [34490.0, 0.631], [34489.9, 5.027], [34489.7, 0.005], [34489.6, 0.008], [34489.5, 0.003], [34489.4, 3.595], [34489.3, 0.049], [34489.2, 0.48], [34489.1, 0.021], [34489.0, 0.258], [34488.9, 0.016], [34488.8, 0.001], [34488.7, 0.502], [34488.5, 0.51], [34488.4, 0.035], [34488.3, 0.058], [34488.2, 0.1], [34488.1, 0.011], [34488.0, 1.402], [34487.9, 0.004], [34487.8, 0.526], [34487.6, 0.01], [34487.5, 0.453], [34487.4, 0.48], [34487.3, 0.068], [34487.2, 0.411], [34487.1, 1.315], [34487.0, 0.203], [34486.9, 0.03], [34486.7, 0.534], [34486.6, 0.003], [34486.5, 0.014], [34486.4, 0.477], [34486.3, 0.086], [34486.2, 1.287], [34486.1, 0.054], [34486.0, 0.151], [34485.8, 0.171], [34485.7, 0.006], [34485.6, 0.479], [34485.5, 0.013], [34485.4, 0.006], [34485.3, 0.002], [34485.2, 0.042], [34485.1, 4.02], [34485.0, 5.442], [34484.9, 9.061], [34484.6, 0.426], [34484.5, 1.747], [34484.3, 0.96], [34484.1, 0.008], [34484.0, 0.88], [34483.9, 0.009], [34483.8, 0.006], [34483.6, 0.003]], 
    'asks': [[34539.1, 25.598], [34539.2, 0.003], [34539.3, 0.068], [34539.4, 0.068], [34539.8, 0.032], [34540.0, 0.546], [34540.1, 0.075], [34540.2, 0.004], [34540.3, 0.003], [34540.5, 2.932], [34540.7, 0.461], [34540.8, 0.059], [34541.0, 0.003], [34541.1, 0.003], [34541.2, 0.068], [34541.3, 0.419], [34541.5, 0.249], [34541.6, 0.145], [34541.9, 0.585], [34542.0, 0.207], [34542.1, 1.025], [34542.2, 0.618], [34542.3, 0.029], [34542.5, 0.023], [34542.6, 0.672], [34542.8, 0.172], [34542.9, 0.189], [34543.0, 0.458], [34543.2, 0.039], [34543.3, 0.054], [34543.4, 0.075], [34543.5, 0.065], [34543.6, 0.683], [34543.7, 0.149], [34543.8, 0.37], [34543.9, 0.014], [34544.0, 0.087], [34544.1, 0.449], [34544.2, 0.003], [34544.3, 0.007], [34544.4, 0.324], [34544.5, 0.066], [34544.7, 0.233], [34544.8, 1.091], [34544.9, 0.691], [34545.0, 0.23], [34545.1, 1.411], [34545.2, 0.435], [34545.3, 0.048], [34545.4, 0.09], [34545.5, 0.013], [34545.6, 0.031], [34545.7, 0.004], [34545.8, 0.813], [34545.9, 1.548], [34546.0, 1.429], [34546.1, 0.019], [34546.2, 0.084], [34546.3, 0.814], [34546.4, 1.0], [34546.5, 4.578], [34546.7, 0.112], [34546.8, 0.22], [34546.9, 0.036], [34547.0, 0.254], [34547.1, 0.004], [34547.2, 0.148], [34547.3, 0.026], [34547.4, 1.393], [34547.5, 0.128], [34547.6, 1.278], [34547.7, 0.934], [34547.8, 1.048], [34548.0, 1.55], [34548.1, 0.366], [34548.2, 0.22], [34548.3, 1.504], [34548.4, 0.152], [34548.5, 0.073], [34548.6, 0.003], [34548.8, 0.292], [34548.9, 1.916], [34549.0, 2.321], [34549.1, 0.066], [34549.3, 0.818], [34549.5, 0.952], [34549.6, 0.101], [34549.7, 0.011], [34549.8, 0.152], [34549.9, 0.235], [34550.0, 2.047], [34550.1, 0.942], [34550.2, 0.587], [34550.3, 1.1], [34550.4, 2.166], [34550.5, 0.275], [34550.6, 3.244], [34550.7, 2.538], [34550.8, 0.952], [34550.9, 1.92], [34551.0, 0.558], [34551.1, 0.113], [34551.2, 1.949], [34551.5, 0.003], [34551.6, 0.058], [34551.7, 1.403], [34551.8, 0.014], [34551.9, 2.223], [34552.0, 2.024], [34552.1, 0.095], [34552.2, 4.109], [34552.3, 0.004], [34552.4, 0.624], [34552.5, 0.892], [34552.6, 1.289], [34552.7, 2.029], [34552.8, 0.14], [34552.9, 0.007], [34553.0, 0.003], [34553.1, 0.095], [34553.2, 0.156], [34553.3, 0.438], [34553.4, 0.541], [34553.5, 0.559], [34553.6, 0.141], [34553.7, 0.323], [34553.8, 2.658], [34553.9, 0.541], [34554.0, 0.302], [34554.2, 0.967], [34554.3, 0.391], [34554.4, 1.446], [34554.5, 0.528], [34554.6, 0.514], [34554.8, 0.136], [34554.9, 0.013], [34555.0, 1.027], [34555.1, 0.039], [34555.2, 0.473], [34555.3, 0.102], [34555.4, 0.309], [34555.5, 0.066], [34555.7, 0.003], [34555.8, 1.51], [34555.9, 1.477], [34556.0, 0.53], [34556.4, 1.428], [34556.5, 0.913], [34556.6, 0.319], [34556.7, 0.284], [34556.8, 0.016], [34556.9, 1.257], [34557.0, 0.021], [34557.1, 0.314], [34557.2, 1.345], [34557.3, 0.1], [34557.4, 1.093], [34557.5, 0.007], [34557.6, 0.65], [34557.7, 0.058], [34557.8, 0.781], [34557.9, 0.293], [34558.0, 0.674], [34558.1, 0.058], [34558.3, 0.168], [34558.4, 3.353], [34558.5, 1.51], [34558.6, 0.106], [34558.7, 0.165], [34558.9, 1.163], [34559.0, 0.23], [34559.2, 1.928], [34559.3, 0.107], [34559.4, 0.023], [34559.5, 0.357], [34559.6, 0.66], [34559.7, 0.031], [34559.8, 0.016], [34559.9, 5.049], [34560.0, 15.123], [34560.1, 0.692], [34560.2, 0.11], [34560.3, 0.131], [34560.4, 0.368], [34560.5, 6.009], [34560.6, 0.105], [34560.7, 0.308], [34560.8, 0.058], [34560.9, 0.305], [34561.0, 0.014], [34561.1, 0.029], [34561.2, 0.087], [34561.3, 0.182], [34561.4, 0.015], [34561.5, 1.012], [34561.6, 0.112], [34561.7, 0.16], [34561.8, 0.023], [34561.9, 0.578], [34562.0, 0.048], [34562.1, 0.008], [34562.2, 0.006], [34562.3, 1.839], [34562.4, 0.108], [34562.5, 0.709], [34562.6, 0.721], [34562.7, 0.168], [34562.8, 0.003], [34562.9, 0.619], [34563.0, 0.003], [34563.1, 0.003], [34563.2, 0.004], [34563.3, 0.011], [34563.4, 0.345], [34563.5, 0.031], [34563.6, 0.023], [34563.7, 0.32], [34563.8, 0.64], [34563.9, 3.046], [34564.0, 0.006], [34564.1, 0.058], [34564.2, 0.602], [34564.3, 0.043], [34564.4, 1.294], [34564.5, 0.155], [34564.6, 0.058], [34564.8, 0.061], [34564.9, 4.907], [34565.0, 5.038], [34565.2, 0.003], [34565.3, 0.102], [34565.5, 0.076], [34565.6, 0.083], [34565.7, 0.058], [34565.8, 1.244], [34565.9, 0.158], [34566.0, 0.22], [34566.1, 0.069], [34566.2, 0.107], [34566.3, 0.039], [34566.4, 0.058], [34566.5, 0.753], [34566.6, 0.029], [34566.7, 0.081], [34566.8, 0.006], [34566.9, 0.009], [34567.0, 0.266], [34567.1, 0.105], [34567.2, 0.294], [34567.4, 0.039], [34567.5, 0.07], [34567.6, 1.446], [34567.8, 1.272], [34567.9, 0.047], [34568.0, 0.063], [34568.1, 7.0], [34568.2, 0.004], [34568.3, 0.051], [34568.4, 1.309], [34568.5, 0.438], [34568.6, 0.028], [34568.7, 0.001], [34568.9, 0.29], [34569.0, 0.003], [34569.1, 0.878], [34569.2, 0.004], [34569.3, 0.01], [34569.4, 0.003], [34569.5, 0.469], [34569.6, 0.296], [34569.7, 0.003], [34569.8, 2.719], [34569.9, 0.53], [34570.0, 0.185], [34570.1, 0.549], [34570.2, 0.06], [34570.5, 0.006], [34570.6, 0.294], [34570.7, 0.058], [34570.8, 0.012], [34571.0, 0.184], [34571.1, 0.253], [34571.2, 0.05], [34571.3, 0.12], [34571.4, 0.112], [34571.5, 0.003], [34571.7, 0.393], [34572.0, 0.084], [34572.1, 1.0], [34572.2, 0.043], [34572.3, 0.01], [34572.4, 0.058], [34572.5, 0.006], [34572.6, 0.343], [34572.7, 0.021], [34572.8, 0.01], [34572.9, 0.069], [34573.0, 0.225], [34573.1, 1.021], [34573.2, 0.826], [34573.3, 4.5], [34573.4, 0.073], [34573.5, 0.003], [34573.6, 0.003], [34573.8, 0.001], [34574.0, 1.491], [34574.1, 0.869], [34574.2, 0.145], [34574.3, 1.074], [34574.4, 0.334], [34574.5, 4.934], [34574.6, 0.008], [34574.8, 3.568], [34574.9, 0.016], [34575.0, 0.057], [34575.1, 3.251], [34575.3, 0.703], [34575.4, 0.197], [34575.5, 0.003], [34575.6, 0.256], [34575.7, 0.179], [34575.8, 0.061], [34575.9, 1.445], [34576.0, 1.268], [34576.1, 0.058], [34576.3, 1.02], [34576.4, 3.245], [34576.5, 4.164], [34576.6, 3.037], [34576.7, 0.01], [34576.8, 0.289], [34576.9, 0.018], [34577.0, 0.092], [34577.1, 3.0], [34577.2, 0.037], [34577.3, 0.052], [34577.4, 0.213], [34577.5, 3.461], [34577.6, 0.001], [34577.8, 3.03], [34577.9, 0.653], [34578.0, 0.01], [34578.2, 0.087], [34578.4, 2.552], [34578.5, 0.003], [34578.6, 1.068], [34578.8, 3.5], [34578.9, 0.006], [34579.0, 0.003], [34579.1, 3.893], [34579.2, 0.058], [34579.3, 3.0], [34579.4, 1.537], [34579.5, 0.003], [34579.7, 0.004], [34579.8, 0.827], [34579.9, 0.011], [34580.0, 1.052], [34580.2, 3.0], [34580.3, 1.076], [34580.4, 6.0], [34580.5, 0.007], [34580.6, 0.005], [34580.7, 0.001], [34580.8, 0.115], [34580.9, 4.5], [34581.0, 0.004], [34581.1, 0.195], [34581.2, 0.006], [34581.3, 0.043], [34581.4, 0.269], [34581.5, 0.006], [34581.6, 0.058], [34581.7, 0.062], [34581.9, 6.058], [34582.0, 0.003], [34582.1, 3.31], [34582.2, 8.314], [34582.3, 0.004], [34582.4, 3.0], [34582.5, 0.212], [34582.6, 0.009], [34582.8, 24.568], [34582.9, 0.061], [34583.0, 0.008], [34583.1, 0.155], [34583.3, 0.698], [34583.4, 0.034], [34583.5, 0.009], [34583.8, 0.015], [34583.9, 2.075], [34584.0, 0.145], [34584.1, 0.004], [34584.2, 0.094], [34584.3, 0.144], [34584.4, 0.058], [34584.5, 8.503], [34584.6, 0.019], [34584.7, 0.001], [34584.8, 0.012], [34584.9, 0.01], [34585.0, 0.291], [34585.1, 0.004], [34585.2, 3.354], [34585.3, 0.028], [34585.5, 0.007], [34585.6, 1.945], [34585.7, 1.931], [34585.8, 10.578], [34585.9, 0.362], [34586.0, 0.081], [34586.1, 0.058], [34586.4, 2.914], [34586.5, 1.136], [34586.6, 0.235], [34586.7, 2.888], [34586.8, 0.007], [34586.9, 0.015], [34587.0, 0.223], [34587.1, 0.178], [34587.2, 0.003], [34587.4, 0.008], [34587.5, 0.021], [34587.6, 0.503], [34587.9, 0.163], [34588.0, 2.514], [34588.1, 0.013], [34588.2, 0.142], [34588.4, 0.005], [34588.5, 0.003], [34588.6, 0.008], [34588.7, 0.597], [34588.8, 0.169], [34588.9, 0.336], [34589.0, 0.003], [34589.2, 3.0], [34589.3, 0.278], [34589.4, 0.073], [34589.5, 0.003], [34589.7, 0.032], [34589.8, 0.145], [34589.9, 0.014], [34590.0, 0.165], [34590.3, 1.536], [34590.4, 0.292], [34590.5, 0.005], [34590.7, 3.0], [34590.9, 0.116], [34591.0, 0.034], [34591.1, 5.058], [34591.3, 0.011], [34591.4, 1.445], [34591.5, 3.5], [34591.6, 2.608], [34591.7, 0.12], [34591.8, 0.014], [34591.9, 0.003], [34592.0, 0.046], [34592.1, 0.158], [34592.3, 0.009], [34592.4, 5.58], [34592.6, 0.374], [34592.7, 0.28], [34592.8, 8.5], [34592.9, 0.01], [34593.0, 0.119], [34593.1, 0.058], [34593.3, 0.01], [34593.4, 0.003], [34593.5, 0.38], [34593.7, 0.046], [34593.8, 0.008], [34594.0, 1.556], [34594.2, 0.001], [34594.3, 3.026], [34594.4, 6.315], [34594.5, 0.002], [34594.7, 0.058], [34594.8, 0.005], [34594.9, 0.083], [34595.0, 0.603], [34595.1, 0.021], [34595.2, 3.307], [34595.3, 3.934], [34595.4, 0.002], [34595.5, 0.065], [34595.6, 0.298], [34595.7, 0.632], [34595.8, 0.081], [34595.9, 18.237], [34596.0, 4.914], [34596.3, 0.247], [34596.5, 0.509], [34596.6, 1.626], [34596.7, 0.004], [34596.8, 0.499], [34597.2, 0.02], [34597.3, 0.007], [34597.4, 1.729], [34597.5, 8.963]], 
    'timestamp': 1699020613278, 
    'datetime': '2023-11-03T14:10:13.278Z', 
    'nonce': 3440561520625
}

'''

# https://github.com/binance/binance-futures-connector-python
cmFuturesClient = CMFutures(key=binanceKey, secret=binanceSecret)
# print(cmFuturesClient.time())

# https://github.com/binance/binance-futures-connector-python/blob/main/examples/cm_futures/market/depth.py
# print(cmFuturesClient.depth("BTCUSD_PERP", **{"limit": 5}))

'''
{   'lastUpdateId': 768744619538, 
    'E': 1699021115927, 
    'T': 1699021115918, 
    'symbol': 'BTCUSD_PERP', 
    'pair': 'BTCUSD', 
    'bids': [['34557.0', '2324'], ['34556.9', '1'], ['34556.7', '1'], ['34556.6', '38'], ['34556.2', '1']], 
    'asks': [['34557.1', '6138'], ['34557.2', '1'], ['34558.3', '1050'], ['34558.4', '307'], ['34558.5', '1']]
}

'''

# https://github.com/binance/binance-futures-connector-python/blob/main/examples/cm_futures/market/trades.py
# print(cmFuturesClient.trades("BTCUSD_PERP", limit=500))

'''
[   {'id': 680936778, 'price': '34542.5', 'qty': '10', 'baseQty': '0.02894984', 'time': 1699021068647, 'isBuyerMaker': False}, 
    {'id': 680936779, 'price': '34542.9', 'qty': '1000', 'baseQty': '2.89495092', 'time': 1699021068647, 'isBuyerMaker': False}, 
]
'''

