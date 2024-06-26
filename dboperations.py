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

# Store procedure para actualizar datos
def act_dolar(pamount):
    conn = conection()
    try:
     # create a cursor object for execution
     cursor = conn.cursor()
     cursor.execute("BEGIN")
     cursor.callproc('act_dolar', (pamount, ))  # Llamado de procedimiento almacenado en postgres
     cursor.execute("COMMIT")
     cursor.close  # Cerrar cursor
     # Llamado de store procedure para actualizar tabla t_historical
    except (psycopg2.DatabaseError) as error:
          print(error)
    finally:
        if conn is not None:
            conn.close()  # Cerrando conección
    return    


import psycopg2
from psycopg2 import sql

def act_prices_batch(data):
    # Connect to your postgres DB
    conn = psycopg2.connect(host="134.209.45.101", database="p2p", user="p2p", password="p42fUEoUpfAp2b7QsibgIT4PCWrp4wCW")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # SQL query for deleting old records
    delete_query = sql.SQL("DELETE FROM p2p_prices WHERE crypto = %s AND fiat = %s")

    # SQL query for inserting new records
    insert_query = sql.SQL("INSERT INTO p2p_prices (crypto, fiat, value, date) VALUES (%s, %s, %s, CURRENT_DATE)")

    try:
        for item in data:
            # Delete old record
            cur.execute(delete_query, (item[0], item[1]))

            # Insert new record
            cur.execute(insert_query, item)

        # Commit the transaction
        conn.commit()
    except Exception as e:
        print(f"Failed to insert data into database. {e}")
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()    