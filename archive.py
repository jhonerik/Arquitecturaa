import datetime

# --- Enunciado del Ejercicio ---
# Crea un programa que pida al usuario su nombre y edad,
# y luego le diga en qué año cumplirá 100 años.

print("--- Calculadora del Centenario ---")

# 1. Pedir el nombre al usuario
nombre_usuario = input("Por favor, introduce tu nombre: ")

# 2. Pedir la edad al usuario y asegurarse de que sea un número válido
while True:
    try:
        edad_usuario_str = input(f"Hola {nombre_usuario}, ahora introduce tu edad: ")
        edad_usuario = int(edad_usuario_str)
        break  # Si la conversión a número es exitosa, salimos del bucle
    except ValueError:
        # Si el usuario no introduce un número, mostramos un error y volvemos a pedir la edad.
        print("Error: Debes introducir un número válido para tu edad. Inténtalo de nuevo.")

# 3. Calcular el año en que cumplirá 100 años
año_actual = datetime.datetime.now().year
años_que_faltan_para_100 = 100 - edad_usuario
año_del_centenario = año_actual + años_que_faltan_para_100

# 4. Mostrar el resultado final al usuario
print("\n--- ¡Aquí está tu resultado! ---")
print(f"¡Qué bien, {nombre_usuario}!")
print(f"Cumplirás 100 años en el año {año_del_centenario}.")

