from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
from datetime import datetime

now = datetime.now()
day = now.strftime("%d%m%Y")

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'INR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '685a87cb-6f85-49a1-b2b4-3e33959625f5',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

dataset = pd.json_normalize(data['data'])
current_local_timestamp = pd.Timestamp.now()
dataset['timestamp'] = current_local_timestamp.replace(tzinfo=None)

dataset.to_excel(f'Crypto_DATAset-{day}.xlsx', index=False)
