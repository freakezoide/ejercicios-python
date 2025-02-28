#dicc = {'one': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco'}

#for elem in dicc.keys():
    #print(type(elem))
    #print(elem)
"""
dicc = {}
cadena = "Mississippi"
for letra in cadena:
    dicc[letra] = dicc.get(letra, 0) + 1
    #if letra in dicc:
    #    dicc[letra] += 1   # dicc[letra] = dicc[letra] + 1
    #else:
    #    dicc[letra] = 1
"""
#print(dicc)
'''
3. Escribir un programa que guarde en un diccionario los precios de las frutas de 
la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
diccionario debe mostrar un mensaje informando de ello. Repetir las preguntas 
hasta que el usuario ingrese la palabra  fin (fin puede estar en mayúsculas o 
minúsculas). 
Fruta 
Banana 
Manzana 
Pera 
Naranja 
Precio 
1.35 
0.80 
0.85 
0.70 

1 - Menu
    1.1 - Guardar fruta y su precio
    1.2 - Consultar precio de fruta
    1.3 - Preguntar por fruta y kilos
    1.4 - Fin
'''
#Inicialización de variables
salida = False
dicc_frutas = {}    #dicc_frutas = dict()
def imprimir_menu():    #Función para imprimir el menú
    print("1 - Menu")
    print("---------------------------------")
    print("a - Guardar fruta y su precio")
    print("b - Consultar precio de fruta")
    print("c - Preguntar por fruta y kilos")
    print("d - Fin")

def ingreso_fruta(fruta, precio):   #Función que agrega frutas y su precio al diccionario
    dicc_frutas[fruta.lower()] = precio

def consulta_precio(fruta):     #Función que consulta el precio de una fruta
    precio = dicc_frutas.get(fruta.lower(), -1)
    return precio

while not salida:   # while salida == False
    imprimir_menu() #Llamada a función menú
    opcion = input("Por favor ingrese una opción: ").lower()    #.lower() convierte a minúsculas el input

    if opcion == "a":
        #print("Guardar fruta y su precio")
        fruta = input("Ingrese la fruta: ")
        precio = float(input("Ingrese el precio: "))
        ingreso_fruta(fruta, precio)    #Llamada a función ingreso_fruta
    elif opcion == "b":
        #print("Consultar precio de fruta")
        fruta = input("Ingrese la fruta: ")
        precio_f = consulta_precio(fruta)   #Llamada a función consulta_precio

        if precio_f == -1:
            print("La fruta no se encuentra en el diccionario")
        else:
            print(f"El precio de la fruta {fruta} es {precio_f}")
    elif opcion == "c":
        #print("Preguntar por fruta y kilos")
        fruta = input("Ingrese la fruta: ")
        kilos = float(input("Ingrese la cantidad de kilos: "))

        precio_f = consulta_precio(fruta)   #Llamada a función consulta_precio

        if precio_f == -1:
            print("La fruta no se encuentra en el diccionario")
        else:
            precio_fruta_final = precio_f * kilos
            print(f"El precio de {kilos} kilos de la fruta {fruta} es {precio_fruta_final:.2f}")
    elif opcion == "d":
        salida = True
        print("Muchas gracias por utilizar el programa")
    else:
        print("Opción inválida")
