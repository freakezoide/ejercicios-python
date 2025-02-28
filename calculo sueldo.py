def calcular_antiguedad(sueldo_acordado, anios_antiguedad):
    if anios_antiguedad >= 20:
        return sueldo_acordado * 0.20
    else:
        return sueldo_acordado * (anios_antiguedad * 0.01)

def calcular_seguro_retiro(sueldo_bruto):
    return sueldo_bruto * 0.11

def calcular_seguro_medico(sueldo_bruto):
    return sueldo_bruto * 0.06

def calcular_impuesto_ganancia(sueldo_bruto):
    if sueldo_bruto > 120000:
        return sueldo_bruto * 0.25
    elif sueldo_bruto > 70000:
        return sueldo_bruto * 0.20
    else:
        return 0

def calcular_sueldo_final(sueldo_acordado, anios_antiguedad):
    # Cálculo de antigüedad
    adicional_antiguedad = calcular_antiguedad(sueldo_acordado, anios_antiguedad)
    sueldo_bruto = sueldo_acordado + adicional_antiguedad

    # Cálculo de descuentos
    descuento_retiro = calcular_seguro_retiro(sueldo_bruto)
    descuento_medico = calcular_seguro_medico(sueldo_bruto)
    descuento_ganancia = calcular_impuesto_ganancia(sueldo_bruto)

    sueldo_neto = sueldo_bruto - (descuento_retiro + descuento_medico + descuento_ganancia)

    return {
        "sueldo_bruto": sueldo_bruto,
        "adicional_antiguedad": adicional_antiguedad,
        "descuento_retiro": descuento_retiro,
        "descuento_medico": descuento_medico,
        "descuento_ganancia": descuento_ganancia,
        "sueldo_neto": sueldo_neto
    }

# Solicitar datos al usuario
try:
    sueldo_acordado = float(input("Ingrese el sueldo acordado: "))
    anios_antiguedad = int(input("Ingrese los años de antigüedad: "))

    # Calcular y mostrar resultados
    resultados = calcular_sueldo_final(sueldo_acordado, anios_antiguedad)
    print("\nResultados del cálculo:")
    print(f"Sueldo Bruto: ${resultados['sueldo_bruto']:.2f}")
    print(f"Adicional por Antigüedad: ${resultados['adicional_antiguedad']:.2f}")
    print(f"Descuento Seguro de Retiro: ${resultados['descuento_retiro']:.2f}")
    print(f"Descuento Seguro Médico: ${resultados['descuento_medico']:.2f}")
    print(f"Impuesto a la Ganancia: ${resultados['descuento_ganancia']:.2f}")
    print(f"Sueldo Neto: ${resultados['sueldo_neto']:.2f}")
except ValueError:
    print("Por favor, ingrese valores válidos para el sueldo y la antigüedad.")