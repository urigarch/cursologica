# OBTENER LOS VALORES: a, b y c. CALCULAR LA FORMULA GENERAL.
# ENTRADA DE DATOS 

a = float(input("introduzca el valor de a: "))
b = float(input("introduzca el valor de b: "))
c = float(input("introduzca el valor de c: "))


# PROCESO DE CALCULOS
x1 = (-b-(((b**2)-(4*a*c))**.5))/(2*a)
x2 = (-b+(((b**2)-(4*a*c))**.5))/(2*a)


# SALIDA DE DATOS 

print("valor de x1",round(x1,2))
print("valor de X2",round(x2,2))
