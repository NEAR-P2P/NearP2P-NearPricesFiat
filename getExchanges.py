# import pandas as pd
import ccxt
import psycopg2
from  decimal import *
import multiprocessing
from datetime import datetime
import time

def conection():
    conn = psycopg2.connect(host="localhost", database="biterchecker", user="openbizview", password="openbizview")
    return conn

# Store procedure para actualizar datos
def act_asset(pexchange, passet, pamount):
    conn = conection()
    try:
     # create a cursor object for execution
     cursor = conn.cursor()
     cursor.execute("BEGIN")
     cursor.callproc('act_asset', (pexchange, passet, pamount,))  # Llamado de procedimiento almacenado en postgres
     cursor.execute("COMMIT")
     cursor.close  # Cerrar cursor
     # Llamado de store procedure para actualizar tabla t_historical
    except (psycopg2.DatabaseError) as error:
          print(error)
    finally:
        if conn is not None:
            conn.close()  # Cerrando conección
    return




# Ejecuta toda la operación aprovechando core de equipo
start = datetime.now()
ccxtExchanges("BTC/USDT")
print('Tiempo de ejecución ' + str(datetime.now() - start))
