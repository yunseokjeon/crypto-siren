# Import the requests library
import requests
from jproperties import Properties

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
    'interval': '1d',
    'backtracks': '10'
}

# Send get request and save the response as response object
response = requests.get(url=endpoint, params=parameters)

# Extract data in json format
result = response.json()

# Print result
print(result)
