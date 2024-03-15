import requests
import json
from datetime import datetime
import dboperations

def exec():
   start = datetime.now()
   #api from Coingeko
   url = "https://api.coingecko.com/api/v3/coins/wrapped-bitcoin/tickers/"
   r = requests.get(url)
   

   token_price = float(r.json()["tickers"][0]["last"])
   #
   dboperations.act_prices('WBTC', 'USD', token_price)
   print('Tiempo de ejecución WBTC FIAT ' + str(datetime.now() - start))

# exec()