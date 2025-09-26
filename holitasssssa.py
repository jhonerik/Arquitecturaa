# Programa Interactivo en Python: Adivina el Número

import random

def adivina_el_numero():
    """
    Juego interactivo donde el usuario debe adivinar un número secreto.
    """
    print("¡Bienvenido al juego Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Tienes 7 intentos para adivinarlo.")

    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0

    while intentos_realizados < 7:
        try:
            intento = int(input("Introduce tu adivinanza: "))
            intentos_realizados += 1

            if intento < numero_secreto:
                print("Tu número es muy bajo.")
            elif intento > numero_secreto:
                print("Tu número es muy alto.")
            else:
                print(f"¡Felicidades! ¡Adivinaste el número en {intentos_realizados} intentos!")
                return # Sale de la función si adivina
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    print(f"\n¡Oh no! Te quedaste sin intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivina_el_numero()
