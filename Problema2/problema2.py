import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    fuentes_disponibles = figlet.getFonts()

    fuente_seleccionada = input("Ingrese el nombre de la fuente a utilizar (presione Enter para elegir una fuente aleatoria): ").strip()

    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Se ha seleccionado la fuente aleatoria: {fuente_seleccionada}")
    else:
        if fuente_seleccionada not in fuentes_disponibles:
            print(f"La fuente '{fuente_seleccionada}' no es válida. Se seleccionará una fuente aleatoria.")
            fuente_seleccionada = random.choice(fuentes_disponibles)
            print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")
    
    figlet.setFont(font=fuente_seleccionada)
    texto_imprimir = input("Ingrese el texto que desea imprimir: ")
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()
