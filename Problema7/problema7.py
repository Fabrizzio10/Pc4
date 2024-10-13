import requests
import sqlite3
import pandas as pd
from pymongo import MongoClient

sqlite_db = 'base.db'
sqlite_table = 'sunat_info'

mongo_client = MongoClient("mongodb+srv://pingoaguilarf:zutFNfWkJQKSp0og@clustermongodb.9rwca.mongodb.net/")
mongo_db = mongo_client['sunat_database']
mongo_collection = mongo_db['sunat_info']

def obtener_datos_sunat():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    response = requests.get(url)
    data = response.json()
    
    print(data)
    
    return data

def almacenar_en_sqlite(data):
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {sqlite_table} (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')


    fecha = data['fecha']
    compra = data['compra']
    venta = data['venta']

    cursor.execute(f'''
        INSERT OR REPLACE INTO {sqlite_table} (fecha, compra, venta)
        VALUES (?, ?, ?)
    ''', (fecha, compra, venta))
    
    conn.commit()
    conn.close()

def almacenar_en_mongodb(data):
    mongo_collection.replace_one({'fecha': data['fecha']}, data, upsert=True)

def mostrar_contenido_sqlite():
    conn = sqlite3.connect(sqlite_db)
    df = pd.read_sql_query(f'SELECT * FROM {sqlite_table}', conn)
    print(df)
    conn.close()


def main():
    datos = obtener_datos_sunat()
    almacenar_en_sqlite(datos)

    almacenar_en_mongodb(datos)
    print("Contenido de la tabla en SQLite:")
    mostrar_contenido_sqlite()

if __name__ == "__main__":
    main()