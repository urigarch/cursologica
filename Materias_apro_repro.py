# EJERCICO 1 
# APROBADO > 6 Y <=10
# PANAZAZO == 6
# REPROBADO >= 0 Y <6
# ERROR EN EL PROMEDIO < 0 O > 10

cali1 = float(input("ingrese la primera nota: "))
cali2 = float(input("ingrese la segunda nota: "))
cali3 = float(input("ingrese la tercera nota: "))

promedio = (( cali1 + cali2 + cali3) / 3)
# OPERACIONES


if (promedio > 6 and promedio <= 10):
    print("promedio", round(promedio,2))
    print("APROBADO")

elif (promedio == 6):
    print("promedio", round(promedio,2))
    print(" PANZAZO ")

elif (promedio < 6 and promedio >= 0):
    print("promedio", round(promedio,2))
    print("REPROBADO")

else:
    print("promedio", round(promedio,2))
    print("ERROR EN LA CALIFICACION")



