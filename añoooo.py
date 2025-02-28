def es_bisiesto(anio):
    # Un año es bisiesto si es divisible entre 4, no divisible entre 100, o divisible entre 400
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def fecha_valida(dia, mes, anio):
    # Días máximos para cada mes
    dias_por_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Verificar que el mes sea válido
    if mes < 1 or mes > 12:
        return False

    # Ajustar febrero si el año es bisiesto
    if mes == 2 and es_bisiesto(anio):
        dias_por_mes[2] = 29

    # Verificar que el día sea válido
    return 1 <= dia <= dias_por_mes[mes]


# Solicitar la fecha al usuario
try:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    if fecha_valida(dia, mes, anio):
        print(f"La fecha {dia}/{mes}/{anio} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{anio} no es válida.")
except ValueError:
    print("Por favor, ingrese números enteros válidos para el día, mes y año.")
