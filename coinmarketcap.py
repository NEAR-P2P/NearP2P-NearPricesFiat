 #This example uses Python 2.7 and the python-request library.
from requests import  Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import dboperations
import ars

listSymbol = ["quote.EUR.price"
            , "quote.USD.price"
            , "quote.RUB.price"
            , "quote.VES.price"
            ]

def symbol_name(pos):
      dict = {   1: "EUR"        
               , 2: "USD"
               , 3: "RUB"
               , 4: "VES"}
      return dict.get(pos)     

url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
parameters = {
  'symbol':'NEAR',
   'amount':'1',
   'convert': 'EUR,USD,RUB,VES'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2f48c701-7b9d-485e-8bee-ccd6d981111f',
}

session = Session()
session.headers.update(headers)

try:
  index = 0
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  df = pd.json_normalize(data['data'])
  #print(df)
  for x in listSymbol:
      index += 1
      dboperations.act_prices('NEAR', symbol_name(index), float(df[x][0]))
      #print(symbol_name(index))
      #print(df[x][0])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#Actualizar el precio de la moneda ars
ars.exec()