import ccxt
import pprint
import pandas as pd

# 현재가 조회
binance = ccxt.binance()
markets= binance.load_markets()

print(markets.keys())
print(len(markets))

btc = binance.fetch_ticker("BTC/USDT")
pprint.pprint(btc)

'''

ask	매도 1호가
askVolume	매도 1호과 물량
bid	매수 1호가
bidVolume	매수 1호과 물량
datetime	현재시간
timestamp	타임 스탬프
open	시가
high	고가
low	저가
close	종가
symbol	심볼

{'ask': 34175.17,
 'askVolume': 4.33404,
 'average': 34190.965,
 'baseVolume': 35555.19182,
 'bid': 34175.16,
 'bidVolume': 0.76727,
 'change': -31.61,
 'close': 34175.16,
 'datetime': '2023-10-31T07:47:30.476Z',
 'high': 34856.0,
 'info': {'askPrice': '34175.17000000',
          'askQty': '4.33404000',
          'bidPrice': '34175.16000000',
          'bidQty': '0.76727000',
          'closeTime': '1698738450476',
          'count': '1181784',
          'firstId': '3261580425',
          'highPrice': '34856.00000000',
          'lastId': '3262762208',
          'lastPrice': '34175.16000000',
          'lastQty': '0.11934000',
          'lowPrice': '34062.84000000',
          'openPrice': '34206.77000000',
          'openTime': '1698652050476',
          'prevClosePrice': '34206.77000000',
          'priceChange': '-31.61000000',
          'priceChangePercent': '-0.092',
          'quoteVolume': '1224996810.94131770',
          'symbol': 'BTCUSDT',
          'volume': '35555.19182000',
          'weightedAvgPrice': '34453.38776803'},
 'last': 34175.16,
 'low': 34062.84,
 'open': 34206.77,
 'percentage': -0.092,
 'previousClose': 34206.77,
 'quoteVolume': 1224996810.9413178,
 'symbol': 'BTC/USDT',
 'timestamp': 1698738450476,
 'vwap': 34453.38776803}
 
'''

# 분봉 조회

btc_ohlcv = binance.fetch_ohlcv("BTC/USDT")

df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime', inplace=True)
print(df)

# 일봉 조회

btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", '1d')

df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime', inplace=True)
print(df)

# 호가 조회

orderbook = binance.fetch_order_book('ETH/USDT')
print(orderbook['asks'])
print(orderbook['bids'])







