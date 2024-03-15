import requests
import json
from datetime import datetime
import dboperations

def exec():
   start = datetime.now()
   #api from Coingeko
   url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
   r = requests.get(url)

   token_price = float(r.json()["price"])
   #
   dboperations.act_prices('BTC', 'USD', token_price)
   print('Tiempo de ejecución BTC FIAT ' + str(datetime.now() - start))

#exec()