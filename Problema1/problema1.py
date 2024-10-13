import requests


def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']  
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None


def guardar_bitcoins_en_fichero(nombre_fichero, cantidad_bitcoins):
    try:
        with open(nombre_fichero, 'w') as fichero:
            fichero.write(str(cantidad_bitcoins))
        print(f"Cantidad de Bitcoins guardada en {nombre_fichero}.")
    except IOError:
        print(f"Error al intentar guardar la cantidad de Bitcoins en {nombre_fichero}.")


def guardar_resultado_en_fichero(nombre_fichero, resultado):
    try:
        with open(nombre_fichero, 'w') as fichero:
            fichero.write(resultado)
        print(f"Resultado guardado en {nombre_fichero}.")
    except IOError:
        print(f"Error al intentar guardar el resultado en {nombre_fichero}.")


def main():
    nombre_fichero_entrada = "bitcoins.txt"  
    nombre_fichero_salida = "resultado.txt"  

    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    guardar_bitcoins_en_fichero(nombre_fichero_entrada, n)
    precio_bitcoin = obtener_precio_bitcoin()
    
    if precio_bitcoin is not None:
        valor_total = n * precio_bitcoin
        resultado = f"El valor de {n} Bitcoins es: ${valor_total:,.4f}"
        print(resultado)
        guardar_resultado_en_fichero(nombre_fichero_salida, resultado)
    else:
        print("No se pudo obtener el precio de Bitcoin.")

if __name__ == "__main__":
    main()