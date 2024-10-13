import requests
import zipfile
import os

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

nombre_imagen = "imagen_descargada.jpg"
nombre_zip = "imagen.zip"

def descargar_imagen(url, nombre_imagen):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() 
        with open(nombre_imagen, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f"Imagen descargada: {nombre_imagen}")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

def crear_zip(nombre_imagen, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_imagen)
        print(f"Archivo ZIP creado: {nombre_zip}")
    except Exception as e:
        print(f"Error al crear el archivo ZIP: {e}")

def main():
    descargar_imagen(url, nombre_imagen) 
    crear_zip(nombre_imagen, nombre_zip)
if __name__ == "__main__":
    main()
