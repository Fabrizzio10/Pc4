import sqlite3
import csv

conn = sqlite3.connect('tipo_cambio.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tipo_cambio (
    fecha TEXT PRIMARY KEY,
    tipo_cambio REAL
)
''')

datos_tipo_cambio = [
    ('2024-07-01', 3.75),
    ('2024-07-02', 3.80)
]
cursor.execute('DELETE FROM tipo_cambio')

cursor.executemany('INSERT OR REPLACE INTO tipo_cambio (fecha, tipo_cambio) VALUES (?, ?)', datos_tipo_cambio)
conn.commit()
def obtener_tipo_cambio(fecha):
    cursor.execute("SELECT tipo_cambio FROM tipo_cambio WHERE fecha = ?", (fecha,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None
ventas = []
with open('ventas.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        fecha, producto, cantidad, precio_dolares = row[0], row[1], int(row[2]), float(row[3])
        ventas.append((fecha, producto, cantidad, precio_dolares))
totales = {}
for fecha, producto, cantidad, precio_dolares in ventas:
    tipo_cambio = obtener_tipo_cambio(fecha)
    
    if tipo_cambio is None:
        continue

    precio_total_dolares = cantidad * precio_dolares
    precio_total_soles = precio_total_dolares * tipo_cambio
    
    if producto not in totales:
        totales[producto] = {'dolares': 0, 'soles': 0}
    
    totales[producto]['dolares'] += precio_total_dolares
    totales[producto]['soles'] += precio_total_soles
if not totales:
    print("No se encontraron productos para mostrar.")
else:
    print(f"{'Producto':<15}{'Total en USD':<15}{'Total en Soles':<15}")
    for producto, total in totales.items():
        print(f"{producto:<15}{total['dolares']:<15.2f}{total['soles']:<15.2f}")
conn.close()