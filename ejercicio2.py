# Solicitar dos números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar opciones de operación
print("¿Qué operación desea realizar?")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Digite el número de la operación (1-4): ")

if opcion == '1':
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Opción inválida.")