import os

def contar_lineas_codigo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas_codigo = 0
            for linea in archivo:
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    lineas_codigo += 1
            return lineas_codigo
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta de un archivo .py: ")

    if os.path.isfile(ruta_archivo) and ruta_archivo.endswith('.py'):
        lineas = contar_lineas_codigo(ruta_archivo)
        if lineas is not None:
            print(f"La cantidad de líneas de código en '{ruta_archivo}' es: {lineas}")
    else:
        print("Ruta inválida o el archivo no es un archivo .py.")

if __name__ == "__main__":
    main()
