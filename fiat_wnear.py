import requests
import json
from datetime import datetime
import dboperations

def exec():
   start = datetime.now()
   #api from Coingeko
   url = "https://api.binance.com/api/v3/ticker/price?symbol=NEARUSDT"
   r = requests.get(url)

   token_price = float(r.json()["price"])
   #
   dboperations.act_prices('wNEAR', 'USD', token_price)
   print('Tiempo de ejecución wNEAR FIAT ' + str(datetime.now() - start))

#exec()