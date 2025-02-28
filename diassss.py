dia= int(input ("ingrese el dia de la semana donde 1 corresponde a LUNES , 7 para DOMINGO: "))
if dia == 1:
    print("Hoy comienza la semana. Ánimo!")
elif dia == 5:
    print ("Ya casi termina")
elif dia== 6 or dia==7:
    print("Siiii, Fin de semana!")
elif 1 < dia < 7:
    print("vamos que se puede")
else:
    print("Día invalido, ingrese un numero entre 1 y 7")
2