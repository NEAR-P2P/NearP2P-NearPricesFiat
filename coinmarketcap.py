 #This example uses Python 2.7 and the python-request library.
from requests import  Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import dboperations

listSymbol = ["quote.ARS.price"
            , "quote.CAD.price"
            , "quote.CLP.price"
            , "quote.COP.price"
            , "quote.CRC.price"
            , "quote.CUP.price"
            , "quote.DOP.price"
            , "quote.EUR.price"
            , "quote.GTQ.price"
            , "quote.HNL.price"
            , "quote.INR.price"  
            , "quote.MXN.price"
            , "quote.MYR.price"
            , "quote.PEN.price"
            , "quote.PHP.price"
            , "quote.RUB.price"
            , "quote.SGD.price"
            , "quote.TRY.price"
            , "quote.USD.price"
            , "quote.UYU.price"
            , "quote.VES.price"
            , "quote.VND.price"
            ]

def symbol_name(pos):
      dict = {1: "ARS"
               , 2:  "CAD"
               , 3:  "CLP"
               , 4:  "COP"
               , 5:  "CRC"
               , 6:  "CUP"
               , 7:  "DOP"
               , 8: "EUR"
               , 9: "GTQ"
               , 10: "HNL"
               , 11: "INR"           
               , 12: "MXN"
               , 13: "MYR"
               , 14: "PEN"
               , 15: "PHP"
               , 16: "RUB"
               , 17: "SGD"
               , 18: "TRY" 
               , 19: "USD"
               , 20: "UYU"
               , 21: "VES"
               , 22: "VND"}
      return dict.get(pos)     

url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
parameters = {
  'symbol':'NEAR',
   'amount':'1',
   'convert': 'VES,USD,TRY,INR,MXN,ARS,CLP,COP,CUP,DOP,PHP,UYU,VND,RUB,SGD,PEN,MYR,HNL,GTQ,EUR,CRC,CAD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'xxxx',
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