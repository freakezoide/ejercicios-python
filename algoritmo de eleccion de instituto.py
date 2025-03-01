# Lista de liceos con cupos, puntajes mínimos y distancias
liceos = [
    {"nombre": "Liceo ", "puntaje_minimo": 85, "distancia": 2, "cupos": 3},
    {"nombre": "Instituto ", "puntaje_minimo": 75, "distancia": 5, "cupos": 5},
    {"nombre": "Colegio ", "puntaje_minimo": 80, "distancia": 3, "cupos": 2},
    {"nombre": "UTU", "puntaje_minimo": 70, "distancia": 6, "cupos": 4},
]


def elegir_liceo(puntaje, max_distancia, preferencias):
    posibles_liceos = []

    for liceo in liceos:
        if puntaje >= liceo["puntaje_minimo"] and liceo["distancia"] <= max_distancia and liceo["cupos"] > 0:
            posibles_liceos.append(liceo)

    if not posibles_liceos:
        print("\n❌ No hay liceos disponibles según los criterios.")
        return None

    # Ordenar los liceos según la preferencia del usuario
    posibles_liceos.sort(key=lambda x: (
    preferencias.index(x["nombre"]) if x["nombre"] in preferencias else len(preferencias), x["distancia"]))

    seleccionado = posibles_liceos[0]  # Se elige el mejor liceo según preferencias y distancia
    seleccionado["cupos"] -= 1  # Reducir cupo disponible

    print(f"\n✅ {seleccionado['nombre']} ha sido seleccionado.")
    return seleccionado


def main():
    print("\n🎓 Sistema de Elección de Liceo")
    puntaje = int(input("Ingrese el puntaje del estudiante: "))
    max_distancia = int(input("Ingrese la distancia máxima que desea (en km): "))

    print("\n🏫 Liceos disponibles:")
    for i, liceo in enumerate(liceos, 1):
        print(
            f"{i}. {liceo['nombre']} (Puntaje mínimo: {liceo['puntaje_minimo']}, Distancia: {liceo['distancia']}km, Cupos: {liceo['cupos']})")

    preferencias = input("\nIngrese sus liceos favoritos en orden de preferencia separados por comas: ").split(",")

    resultado = elegir_liceo(puntaje, max_distancia, preferencias)
    if resultado:
        print(f"\n🎉 ¡Felicidades! Ha sido asignado a {resultado['nombre']}.")


if __name__ == "__main__":
    main()
