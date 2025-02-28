import random

# Inicializamos variables
suma_total = 0
cantidad_tiradas = 20



# Simulamos 20 tiradas de dos dados
for _ in range(cantidad_tiradas):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma_tirada = dado1 + dado2
    suma_total += suma_tirada
    print(f"Tirada: Dado 1 = {dado1}, Dado 2 = {dado2}, Suma = {suma_tirada}")

# Calculamos el promedio de la suma de los dos dados
promedio = suma_total / cantidad_tiradas
print(f"\nPromedio de la suma de los resultados de dos dados: {promedio:.2f}")
import random

# Inicializamos el contador para cada cara (1 a 6)
caras = [0] * 6  # Lista para contar las caras [1, 2, 3, 4, 5, 6]
cantidad_tiradas = 30


# Simulamos 20 # tiradas de un dado

for _ in range(cantidad_tiradas):
    resultado = random.randint(1, 6)  # Resultado entre 1 y 6
    caras[resultado - 1] += 1  # Incrementamos el contador para la cara obtenida

# Mostramos los resultados
print("\nCantidad de veces que salió cada cara:")
for i in range(6):
    print(f"Cara {i+1}: {caras[i]} veces")