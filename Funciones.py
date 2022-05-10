# FUNCIONES: Tareas o acciones a ejecutar
# SINTAXIS:
# def Nombre_de_la_funcion(Argumentos o parametros):
#   Contenido de la funcion

# PARADIGMA (enfoque) o modular 
# Secuencial, Selectivo, Iterativo o ciclos (repetitivos)

def Sumar(a, b): # Obtiene o recibe parametros o argumentos
    suma = a + b
    return suma # return: Returnat, devolver o regresar valor

def Restar(num1, num2): # Obtiene o recibe parametros o argumentos
   return num1 - num2

def Division(a, b):
    return a / b

def Multiplicacion(Num1, Num2):
    multipli = Num1 * Num2
    return multipli 

     

# Mandar o llamar o invocar las funciones

num1 = int (input("1er numero : "))
num2 = int (input("2er numero : "))

s = Sumar(num1, num2) # se envian o se pasan los parametros o argumentos
r = Restar(num1,num2)
d = Division(num1,num2)
m = Multiplicacion(num1, num2)

print("La suma es = ", s)
print("La resta es = ", r)
print("La multiplicacion es = ", m)    
print("La division es = ", d)
