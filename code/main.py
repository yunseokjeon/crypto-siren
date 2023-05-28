# Import the requests library
import requests
from jproperties import Properties
from binance.spot import Spot

# application.properties
configs = Properties()
with open('./resource/application.properties', 'rb') as config_file:
    configs.load(config_file)

secretKey = configs.get('TAAPI_KEY')

# Define indicator
indicator = "candle"

# Define endpoint
endpoint = f"https://api.taapi.io/{indicator}"

# Define a parameters dict for the parameters to be sent to the API
parameters = {
    'secret': secretKey,
    'exchange': 'binance',
    'symbol': 'BTC/USDT',
    'interval': '30m',
    'backtracks': '10'
}

# Send get request and save the response as response object
response = requests.get(url=endpoint, params=parameters)

# Extract data in json format
result = response.json()

# Print result
print(result)

# [{'timestampHuman': '2023-05-28 07:30:00 (Sunday) UTC', 'timestamp': 1685259000, 'open': 27198.73, 'high': 27217.81, 'low': 27195.4, 'close': 27201.98, 'volume': 220.25207000000034, 'backtrack': 0}, ... ]


# Binance

client = Spot()

# https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

print(client.klines("BTCUSDT", "30m"))

'''

[   [1684369800000, 
    '27406.85000000', 
    '27420.96000000', 
    '27354.15000000', 
    '27357.42000000', 
    '623.13169000', 
    1684371599999, 
    '17062781.06046580', 
    17031, 
    '326.70465000', 
    '8946781.96350270', 
    '0'], 
    
    ...]
[
  [
    1499040000000,      // Kline open time
    "0.01634790",       // Open price
    "0.80000000",       // High price
    "0.01575800",       // Low price
    "0.01577100",       // Close price
    "148976.11427815",  // Volume
    1499644799999,      // Kline Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "0"                 // Unused field, ignore.
  ]
]
'''


binanceKey = configs.get('BINANCE_KEY')
binanceSecret = configs.get('BINANCE_SECRET')


