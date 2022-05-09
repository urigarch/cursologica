# Pedir el nivel del agua en metros de una cisterna
# Si llega a mas de 6 metros / desbordamiento 
# Nivel de 6 metros / apagar la bomba
# Entre 4 y 6 metros / desacelerar la bomba 
# Entre 2 y 4 metros / bomba trabajando
# De 0 a 2 metros / acelerar bomba
# 0 metros / encender bomba 
# Menor de 0 metros / fuga de cisterna

nivel_agua = int(input("Escribe el nivel del agua: "))

# procesos

if (nivel_agua > 6):
    print("desbordamiento")

elif (nivel_agua == 6):
    print("apagar la bomba")

elif (nivel_agua < 6 and nivel_agua > 4):
    print("desacelerar la bomba")

elif (nivel_agua >= 2 and nivel_agua <=4):
    print("bomba trabajando")

elif (nivel_agua > 0 and nivel_agua < 2):
    print("acelerar bomba")

elif (nivel_agua == 0):
    print("encender bomba")

else:
    print("fuga de cisterna")





