import requests
import json
from datetime import datetime
import dboperations
# from scraping import price

# def exec():
#     url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
#     parameters = {
#       'symbol':'NEAR',
#       'amount':'1',
#       'convert': 'VES,USD'
#     }
#     headers = {
#       'Accepts': 'application/json',
#       'X-CMC_PRO_API_KEY': '0a756f72-99ad-4ee7-be7d-68ed5fd52658',
#     }

#     session = Session()
#     session.headers.update(headers)

#     try:
#       index = 0
#       response = session.get(url, params=parameters)
#       data = json.loads(response.text)
#       df = pd.json_normalize(data['data'])
#       #print(df)
#       for x in listSymbol:
#           index += 1
#           dboperations.act_prices('NEAR', symbol_name(index), float(df[x][0]))
#           #print(symbol_name(index))
#           #print(df[x][0])
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#       print(e)

#     #Actualizar el precio de la moneda ars
#     ars_near.exec()

def exec():
   start = datetime.now()
   #api from Coingeko
   url = "https://api.coingecko.com/api/v3/coins/near/tickers/"
   r = requests.get(url)
   
   #api from dolar scraping
   # precios = price()
   # ves_price = precios
   
   #api dolar blue
   # api from dolar today
   urlars = "https://dolar-api-argentina.vercel.app/v1/dolares/blue"
   rves = requests.get(urlars)
   ars_price = float(rves.json()["venta"])

   # print(r.status_code)

   near_price = float(r.json()["tickers"][0]["last"])
   # ves_near = near_price * ves_price
   ars_near = near_price * ars_price
   # print(ves_near) 
   # #ves  
   # dboperations.act_prices('NEAR', 'VES', ves_near)
   # #ars
   dboperations.act_prices('NEAR', 'ARS', ars_near)
   #
   dboperations.act_prices('NEAR', 'USD', near_price)
   print('Tiempo de ejecución NEAR FIAT ' + str(datetime.now() - start))

# exec()