def es_palindromo(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios para una comparación precisa
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

      Pedir al usuario que ingrese una palabra o frase
frase = input("Escribe una palabra o frase: ")

        Dividir la frase en palabras
               palabras = frase.split()

              Verificar palabra por palabra si es un palíndromo
                     palindromos = [palabra for palabra in palabras if es_palindromo(palabra)]

Mostrar el resultado
if palindromos:
    print(f"Las siguientes palabras son palíndromos: {', '.join(palindromos)}.")
else:
    print("No se encontraron palíndromos en la frase.")