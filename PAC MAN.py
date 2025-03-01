import pygame
import random

# Inicializar pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Configuración de la pantalla
ANCHO, ALTO = 600, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man")

# Tamaño de los bloques
TAMANO_BLOQUE = 30

# Laberinto (1 = pared, 0 = espacio libre, 2 = punto)
laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Posición inicial de Pac-Man
pac_x, pac_y = 1, 1

# Posición inicial del fantasma
fantasma_x, fantasma_y = 18, 1

# Dirección del movimiento
mov_x, mov_y = 0, 0

# Fuente para mostrar la puntuación
fuente = pygame.font.Font(None, 36)

# Puntuación inicial
puntos = 0

# Bucle principal del juego
jugando = True
while jugando:
    pantalla.fill(NEGRO)

    # Capturar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                mov_x, mov_y = -1, 0
            elif evento.key == pygame.K_RIGHT:
                mov_x, mov_y = 1, 0
            elif evento.key == pygame.K_UP:
                mov_x, mov_y = 0, -1
            elif evento.key == pygame.K_DOWN:
                mov_x, mov_y = 0, 1

    # Movimiento de Pac-Man
    nueva_x, nueva_y = pac_x + mov_x, pac_y + mov_y
    if laberinto[nueva_y][nueva_x] != 1:  # Verificar si no es una pared
        pac_x, pac_y = nueva_x, nueva_y

    # Comer puntos
    if laberinto[pac_y][pac_x] == 2:
        laberinto[pac_y][pac_x] = 0
        puntos += 10

    # Movimiento del fantasma (movimiento aleatorio)
    direccion = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
    nueva_fx, nueva_fy = fantasma_x + direccion[0], fantasma_y + direccion[1]
    if laberinto[nueva_fy][nueva_fx] != 1:
        fantasma_x, fantasma_y = nueva_fx, nueva_fy

    # Verificar colisión con el fantasma
    if pac_x == fantasma_x and pac_y == fantasma_y:
        print("👻 ¡Perdiste! Pac-Man fue atrapado.")
        jugando = False

    # Dibujar laberinto
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            x, y = columna * TAMANO_BLOQUE, fila * TAMANO_BLOQUE
            if laberinto[fila][columna] == 1:
                pygame.draw.rect(pantalla, AZUL, (x, y, TAMANO_BLOQUE, TAMANO_BLOQUE))
            elif laberinto[fila][columna] == 2:
                pygame.draw.circle(pantalla, BLANCO, (x + 15, y + 15), 5)

    # Dibujar a Pac-Man
    pygame.draw.circle(pantalla, AMARILLO, (pac_x * TAMANO_BLOQUE + 15, pac_y * TAMANO_BLOQUE + 15), 15)

    # Dibujar al fantasma
    pygame.draw.circle(pantalla, ROJO, (fantasma_x * TAMANO_BLOQUE + 15, fantasma_y * TAMANO_BLOQUE + 15), 15)

    # Mostrar la puntuación
    texto = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    pygame.time.delay(200)

pygame.quit()
