# FUNCIONES DE MERCADOTECNIA:
# 1.- Publicidad
# 2.- Estudio de Mercado
# 3.- Precios productos / servicios
# 4.- Logistica 
# 5.- Ventas 

def Publicidad(cantidad_banner, costo_banner):
    total_costos_banner = cantidad_banner * costo_banner
    print("total costo banner", total_costos_banner)  

def Logistica(transporteA, transporteB):
    total_distancia_transportar = transporteA + transporteB
    if (total_distancia_transportar >= distancia_minima and total_distancia_transportar <= distancia_maxima):
        costo_logistico = (transporteA + transporteB)*distancia_maxima   
    else:
        costo_logistico = (transporteA + transporteB)*distancia_minima  
    
    print("Total de distancia a transportar = ", total_distancia_transportar)
    print("Costo logistico = ", costo_logistico)

def Ventas(cantidad_productos, costo_producto):
    total_ventas = (cantidad_productos + costo_producto) * IVA
    print("Total ventas", total_ventas)

def Precios(costo_fabricacion, costo_almacen): 
    total_precios = (costo_fabricacion + costo_almacen) * IVA
    print("Total precios", total_precios)

def Estudios(costo_encuestas, procesar_datos):
    total_estudios = (costo_encuestas + procesar_datos )
    print("Total estudios", total_estudios)

def Menu():
    print("******MERCADOTECNIA******")
    print("1.- Publicidad")
    print("2.- Estudio de Mercado")  
    print("3.- precios productos/servicios  ")
    print("4.- logistica")
    print("5.- ventas")

# ENTRADA DE DATOS

costo_banner = 100
cantidad_banner = 1000

transporteA = 10
transporteB = 20 
distancia_maxima = 5
distancia_minima = 2


cantidad_productos = 1000
costo_producto = 50
IVA = 0.16

costo_fabricacion = 30
costo_almacen = 15

costo_encuestas = 200 
procesar_datos = 150

respuesta = "si"
opcion = 0

while (respuesta == "si"):
    Menu()
    opcion = int(input("Elige la opcion: "))
    if(opcion == 1):
        Publicidad(cantidad_banner, costo_banner)
    elif(opcion == 2):
        Logistica(transporteA, transporteB)  
    elif(opcion == 3):
        Ventas(cantidad_productos, costo_producto)
    elif(opcion == 4):    
        Precios(costo_fabricacion, costo_almacen)     
    elif(opcion == 5):
        Estudios(costo_encuestas, procesar_datos)
    else:
        print("OPCION INVALIDA")
    respuesta = input("¿Quieres continuar?: ")        
    