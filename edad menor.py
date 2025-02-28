# Solicitar el nombre y la edad del usuario
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))

# Evaluar la edad y generar el mensaje correspondiente
if edad < 18:
    mensaje = f"{nombre}, eres menor de edad."
else:
    mensaje = f"{nombre}, ya eres mayor de edad."

# Imprimir el mensaje
print(mensaje)



