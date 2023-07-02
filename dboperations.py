import psycopg2

def conection():
    conn = psycopg2.connect(host="134.209.45.101", database="p2p", user="p2p", password="p42fUEoUpfAp2b7QsibgIT4PCWrp4wCW")
    return conn

# Store procedure para actualizar datos
def act_prices(pcrypto, pfiat, pamount):
    conn = conection()
    try:
     # create a cursor object for execution
     cursor = conn.cursor()
     cursor.execute("BEGIN")
     cursor.callproc('act_prices', (pcrypto, pfiat, pamount, ))  # Llamado de procedimiento almacenado en postgres
     cursor.execute("COMMIT")
     cursor.close  # Cerrar cursor
     # Llamado de store procedure para actualizar tabla t_historical
    except (psycopg2.DatabaseError) as error:
          print(error)
    finally:
        if conn is not None:
            conn.close()  # Cerrando conección
    return