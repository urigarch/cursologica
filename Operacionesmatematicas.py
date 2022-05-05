# Importar la libreria math para funciones Matematicas
import math
from secrets import randbelow

# ENTRADAS DE DATOS
# DEFINIR LAS VARIABLES DE ENTRADA

numero_1 = int(input("Escribe un numero: "))
numero_2 = int(input("Escribe otro numero: "))



# PROCESOS (Calculos u Operaciones Matemanticas y/o Lógicas)
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

potencia_1 = numero_1 ** numero_2
potencia_2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2, 3)

raiz_cuadrada_1 = pow(9, 1/2)
raiz_cuadrada_2 = math.sqrt(9)
raiz_cubica = pow(27, 1/3)

modulo_residuo = numero_1 % numero_2

#SALIDAS DE DATOS
print("La suma es =", suma)
print(f" La suma es = {suma}") # f: formatear
print("La suma es = " + str(suma)) #CONCATENACION (Union de textos)
# convertir un tipo de dato en otro tipo de dato (CASTEO)

print("La resta es =", resta)
print(f"La resta es = {resta}") # f: formatear
print("La resta es = " + str(resta)) #CONCATENAR (union de textos)

print("La multiplicacion es =", multiplicacion)
print(f"La multiplicacion es = {multiplicacion}") # f: formatear
print("La multiplicacion es = " + str(multiplicacion)) #CONCATENAR (union de textos)

print("La division es =", division)
print(f"La division es = {division}") # f: formatear
print("La division es = " + str(division)) #CONCATENAR (union de textos)

print("La potencia es =", potencia_1)
print(f" La potencia es = {potencia_1}") # f: formatear
print("La potencia es = " + str(potencia_2)) #CONCATENACION (Union de textos)
print("La cuadrado es =", cuadrado)
print(f" El cubo es = {cubo}") # f: formatear
print("La raiz_cuadrada_1 es = " + str(raiz_cuadrada_1)) #CONCATENACION (Union de textos
print("La raiz_cuadrada_2 es =", raiz_cuadrada_2)
print(f" La raiz_cubica es = { raiz_cubica}") # f: formatear

print("El modulo o residuo es = ", modulo_residuo)

