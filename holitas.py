import random

def juego_adivina_el_numero():
    """
    Función principal para el juego de adivinar el número.
    El programa elige un número entre 1 y 100 y el usuario debe adivinarlo.
    """
    print("=======================================")
    print("¡Bienvenido al juego de Adivina el Número!")
    print("=======================================")
    print("He pensado en un número entre 1 y 100. ¿Puedes adivinarlo?")

    # El programa elige un número entero aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0

    # Bucle infinito que se romperá solo cuando el usuario adivine
    while True:
        # 1. Pedimos al usuario que digite algo
        entrada_usuario = input("Introduce tu número: ")
        intentos += 1

        try:
            # 2. Intentamos convertir la entrada a un número entero
            numero_usuario = int(entrada_usuario)

            # 3. Comparamos el número del usuario con el número secreto
            if numero_usuario < numero_secreto:
                print("¡Demasiado bajo! Intenta con un número más alto.")
            elif numero_usuario > numero_secreto:
                print("¡Demasiado alto! Intenta con un número más bajo.")
            else:
                # Si son iguales, el usuario ha ganado
                print(f"🎉 ¡Felicidades! ¡Has adivinado el número en {intentos} intentos! 🎉")
                break  # Rompemos el bucle para terminar el juego

        except ValueError:
            # 4. Si el usuario no introduce un número, se produce un error
            # que capturamos para darle un mensaje amigable.
            print(f"'{entrada_usuario}' no es un número válido. Por favor, intenta de nuevo.")

# Punto de entrada para ejecutar el juego
if __name__ == "__main__":
    juego_adivina_el_numero()

