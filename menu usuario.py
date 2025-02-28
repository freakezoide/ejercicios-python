mayor = 0

while True:
    numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
    if numero == 0:
        break
    if numero > mayor:
        mayor = numero

print(f"El mayor número ingresado fue: {mayor}")