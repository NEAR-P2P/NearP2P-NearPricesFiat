import requests
import json
from datetime import datetime
import dboperations

def exec():
   start = datetime.now()
   #api from Coingeko
   url = "https://api.coingecko.com/api/v3/coins/weth/tickers/"
   r = requests.get(url)
   

   token_price = float(r.json()["tickers"][4]["last"])
   #
   dboperations.act_prices('WETH', 'USD', token_price)
   print('Tiempo de ejecución WETH FIAT ' + str(datetime.now() - start))

# exec()