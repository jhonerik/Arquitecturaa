# Enunciado:
# Escribe un programa en Python que solicite al usuario una lista de números separados por comas,
# y luego calcule y muestre la suma y el promedio de esos números.

def main():
    entrada = input("Ingrese números separados por comas: ")
    numeros = [float(n) for n in entrada.split(",") if n.strip()]
    suma = sum(numeros)
    promedio = suma / len(numeros) if numeros else 0
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")

if __name__ == "__main__":
    main()