def numeros_hailstone():
    # Leer y validar el número inicial
    while True:
        try:
            n = int(input("Ingrese un número entero positivo: "))
            if n > 0:
                break
            else:
                print("El número debe ser un entero positivo. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")

    # Inicializar contador
    contador = 0

    # Mostrar la secuencia de Hailstone
    print("La secuencia de Hailstone es:", n, end="")
    while n != 1:
        if n % 2 == 0:
            n //= 2  # Si es par, dividir entre 2
        else:
            n = (n * 3) + 1  # Si es impar, multiplicar por 3 y sumar 1
        print(f" -> {n}", end="")
        contador += 1  # Incrementar el contador

    # Mostrar el número de transformaciones
    print(f"\nEl número de transformaciones necesarias es: {contador}")


# Llamar a la función
numeros_hailstone()