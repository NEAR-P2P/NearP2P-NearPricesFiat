import json
import requests
import dboperations
from datetime import datetime
import pandas as pd

def exec():
   start = datetime.now()
   #Data from dolarblue
   index = 0
   url = "https://api-dolar-argentina.herokuapp.com/api/dolarblue"
   r = requests.get(url)
   data  = r.json()
   #Data from database
   url1 = "https://nearp2p.com:3070/api/sendmailp2p/get-price"
   # defining a params dict for the parameters to be sent to the API
   r1 = requests.post(url = url1, json = {"fiat": "USD", "crypto": "NEAR"})
   data1 = r1.json()
   #print(data1[0]['value'])
   result = float(data['venta']) * float(data1[0]['value'])
   #print(result)
   if r.status_code == 200:
      dboperations.act_prices('NEAR', 'ARS', float(result))
   # print('Tiempo de ejecución ars ' + str(datetime.now() - start))
