import requests
import json
from datetime import datetime
import dboperations
# from scraping import price

# listSymbol = ["quote.VES.price"
#             , "quote.USD.price"
#             ]

# def symbol_name(pos):
#       dict = {   1: "VES"        
#                , 2: "USD"}
#       return dict.get(pos)  

# def exec():
#     url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
#     parameters = {
#     'symbol':'USDC',
#     'amount':'1',
#     'convert': 'VES,USD'
#     }
#     headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': '2f48c701-7b9d-485e-8bee-ccd6d981111f',
#     }

#     session = Session()
#     session.headers.update(headers)

#     try:
#         index = 0
#         response = session.get(url, params=parameters)
#         data = json.loads(response.text)
#         df = pd.json_normalize(data['data'])
#         #print(df)
#         for x in listSymbol:
#             index += 1
#             dboperations.act_prices('USDC', symbol_name(index), float(df[x][0]))
#             #print(symbol_name(index))
#             #print(df[x][0])
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)

#     #Actualizar el precio de la moneda ars
#     ars_usdc.exec()

def exec():
   start = datetime.now()
   index = 0
   #api from Coingeko
   # url = "https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd"
   # r = requests.get(url)



   # usd_price = float(r.json()["tether"]["usd"])
   #
   #dboperations.act_prices('USDT', 'USD', usd_price)
   #api from dolar Venezuela
   # precios = price()
   # ves_price = precios
   # dboperations.act_prices('USDT', 'VES', ves_price)
   # print(ves_price)
   #api from vercel
   urlars = "https://dolar-api-argentina.vercel.app/v1/dolares/blue"
   rars = requests.get(urlars)
   ars_price = float(rars.json()["venta"])
   dboperations.act_prices('USDT', 'ARS', ars_price)

      #api from api.exchangerate.host
      # urlcop = "https://api.exchangerate.host/latest?base=USD&symbols=COP"
      # rcop = requests.get(urlcop)
      # cop_price = float(rcop.json()["rates"]["COP"])
      # dboperations.act_prices('USDT', 'COP', cop_price)
   
   print('Tiempo de ejecución USDT FIAT ' + str(datetime.now() - start))