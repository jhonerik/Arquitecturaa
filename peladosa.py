import random

def generar_numero_aleatorio():
    """
    Permite al usuario elegir un rango y genera un número aleatorio dentro de ese rango.
    """
    while True:
        print("\n¿En qué rango deseas generar un número aleatorio?")
        print("1. Del 1 al 100")
        print("2. Del 1 al 1000")
        opcion = input("Selecciona una opción (1 o 2): ")

        if opcion == '1':
            limite_inferior = 1
            limite_superior = 100
            break
        elif opcion == '2':
            limite_inferior = 1
            limite_superior = 1000
            break
        else:
            print("Opción inválida. Por favor, selecciona 1 o 2.")

    numero_aleatorio = random.randint(limite_inferior, limite_superior)
    print(f"El número aleatorio generado es: {numero_aleatorio}")

if __name__ == "__main__":
    generar_numero_aleatorio()
