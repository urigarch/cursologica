# ENTRADA DE DATOS
# CALCULA EL PAGO DE NOMINA 

dias = int(input("ingresa la cantidad de dias laborados: "))
salario = float(input("ingrese el salario por dia: "))


#CALCULOS
pago_base = salario * dias
iva_tras = pago_base * .16
subtotal = pago_base + iva_tras
iva_rete = iva_tras/3*2
isr_rete = pago_base * .1
pago_neto = subtotal - ( isr_rete + iva_rete )

#SALIDA DE DATOS
print("pago base", round(pago_base,2))
print("iva trasladado", round(iva_tras,2))
print("subtotal", round(subtotal,2))
print("iva retenido", round(iva_rete,2))
print("isr retenido", round(isr_rete,2))
print("pago neto", round(pago_neto,2))