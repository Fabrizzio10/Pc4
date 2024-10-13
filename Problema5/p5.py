import os

def guardar_tabla_multiplicar(n):
    filename = f'tabla-{n}.txt'
    try:
        with open(filename, 'w') as f:
            for i in range(1, 11):
                f.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla de multiplicar del {n} guardada en '{filename}'.")
    except Exception as e:
        print(f"Error al intentar guardar la tabla: {e}")

def mostrar_tabla(n): 
    filename = f'tabla-{n}.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            contenido = f.read()
            print(contenido)
    else:
        print(f"El fichero '{filename}' no existe.")

def mostrar_linea(n, m):
    filename = f'tabla-{n}.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            lineas = f.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m - 1].strip())
            else:
                print(f"No hay línea {m} en el fichero '{filename}'.")
    else:
        print(f"El fichero '{filename}' no existe.")

def main():
    print("Directorio actual:", os.getcwd()) 
    while True:
        print("\nMenu:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    guardar_tabla_multiplicar(n)
                else:
                    print("Número fuera de rango. Debe ser entre 1 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

        elif opcion == '2':
            try:
                n = int(input("Ingrese un número entero entre 1 y 10 para mostrar la tabla: "))
                if 1 <= n <= 10:
                    mostrar_tabla(n)
                else:
                    print("Número fuera de rango. Debe ser entre 1 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

        elif opcion == '3':
            try:
                n = int(input("Ingrese un número entero entre 1 y 10 para la tabla: "))
                if 1 <= n <= 10:
                    m = int(input("Ingrese el número de la línea que desea mostrar (1-10): "))
                    mostrar_linea(n, m)
                else:
                    print("Número fuera de rango. Debe ser entre 1 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    main()

