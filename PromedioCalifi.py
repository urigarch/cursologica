# ENTRADAS DE DATOS
# DEFINIR LAS VARIABLES DE ENTRADA
# CALCULAR EL PROMEDIO DE 3 CALIFICACIONES Y DECIR SI ES APROBADA O REPROBADO 

cali1 = float(input("ingrese la primera nota"))
cali2 = float(input("ingrese la segunda nota"))
cali3 = float(input("ingrese la tercera nota"))
prom = (cali1+cali2+cali3)/3
if(prom>6):
    prim("su promedio es: ",prom, "aprobado la materia")
else:
    print("su promedio es: ",prom,"reprobo la materia")
    