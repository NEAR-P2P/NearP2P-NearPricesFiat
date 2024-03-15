import requests
import json
from datetime import datetime
import dboperations

def exec():
   start = datetime.now()
   #api from Coingeko
   url = "https://api.coingecko.com/api/v3/coins/ethereum/tickers/"
   r = requests.get(url)
   

   token_price = float(r.json()["tickers"][0]["last"])
   #
   dboperations.act_prices('ETH', 'USD', token_price)
   print('Tiempo de ejecución ETH FIAT ' + str(datetime.now() - start))

# exec()