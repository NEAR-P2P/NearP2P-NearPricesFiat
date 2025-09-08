import requests
import json
from datetime import datetime
import dboperations

def exec():
   print("Iniciando actualización de precios desde Ref Finance...") 
   start = datetime.now()
   #api from Coingeko
   url = "https://indexer.ref.finance/list-token-price"
   r = requests.get(url)

   data = r.json()
   token_data = []
   for token, details in data.items():
       print
       token_price = float(details["price"])
       token_symbol = details["symbol"]
       token_data.append((token_symbol, 'USD', token_price))
    

   # Assuming dboperations.act_prices_batch accepts a list of tuples
   # print(token_data)
   dboperations.act_prices_batch(token_data)

   print('Tiempo de ejecución REF FINANCE FIAT ' + str(datetime.now() - start))


# exec()