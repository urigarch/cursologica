# ENTRADAS DE DATOS
# DEFINIR LAS VARIABLES DE ENTRADA
# PEDIR LA CANTIDAD DE GRADOS Y CONVERTIRLOS A C° F° K


celsius = float(input("ingresar grados celsius: "))
kelvin = float(input("ingresar grados kelvin: "))
fahre = float(input("ingresar grados fahre: "))

# PROCESO DE CALCULOS
kelvin_1 = celsius + 273.15
fahre_1 = (((kelvin-273.15)*9)/5)+32
kelvin_2 = (((fahre-32)*5)/9)+273.15
celsius_1 = kelvin - 273.15

# SALIDA DE DATOS
print("de celsius a kelvin", kelvin_1, "K")
print("de kelvin a fahre", fahre_1, "F")
print("de fahre a kelvin", kelvin_2, "k")
print("de kelvin a celsius", celsius_1, "C")