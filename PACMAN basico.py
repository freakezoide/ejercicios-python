import os

# Mapa del juego: 1 = Pared, 0 = Espacio libre, 2 = Punto
laberinto = [
    "####################",
    "#P   .  ## .   .  #",
    "# #### ## ####### #",
    "#   .   .   .   . #",
    "####################"
]

# Convertimos el mapa en una lista mutable
laberinto = [list(fila) for fila in laberinto]

# Encontrar la posición inicial de Pac-Man
for y in range(len(laberinto)):
    for x in range(len(laberinto[y])):
        if laberinto[y][x] == "P":
            pac_x, pac_y = x, y


# Función para mostrar el mapa en la consola
def mostrar_laberinto():
    os.system("cls" if os.name == "nt" else "clear")
    for fila in laberinto:
        print("".join(fila))


# Contador de puntos
total_puntos = sum(fila.count(".") for fila in laberinto)
puntos = 0

# Bucle principal del juego
while puntos < total_puntos:
    mostrar_laberinto()
    print(f"Puntos: {puntos}/{total_puntos}")

    # Capturar movimiento
    movimiento = input("Mueve (WASD): ").upper()
    nuevo_x, nuevo_y = pac_x, pac_y

    if movimiento == "W":  # Arriba
        nuevo_y -= 1
    elif movimiento == "S":  # Abajo
        nuevo_y += 1
    elif movimiento == "A":  # Izquierda
        nuevo_x -= 1
    elif movimiento == "D":  # Derecha
        nuevo_x += 1

    # Verificar colisión con paredes
    if laberinto[nuevo_y][nuevo_x] != "#":
        # Comer punto si hay
        if laberinto[nuevo_y][nuevo_x] == ".":
            puntos += 1

        # Mover Pac-Man
        laberinto[pac_y][pac_x] = " "  # Dejar espacio vacío atrás
        pac_x, pac_y = nuevo_x, nuevo_y
        laberinto[pac_y][pac_x] = "P"  # Nueva posición de Pac-Man

mostrar_laberinto()
print("🎉 ¡Ganaste! Has recogido todos los puntos.")
wa