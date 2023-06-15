#
print("Hola ! Bienvenido por favor digita los datos solicitados \n")
numeroCuota = int(input("ingresa el numero de cuotas por favor = "))
print(" \n")

costoCuota = int(input("ingresa el Valor de cada cuota ="))
print(" \n")

iva = int(input("Ingresa por favor los intereses mensuales ="))
print(" \n")

valor = (costoCuota*numeroCuota)

impuesto = (valor / 100) * iva 

cuota_iva = (costoCuota + impuesto)*numeroCuota

print("El total a pagar con los impuestos es = ",cuota_iva )
print("\n")
print("el pago sin impuestos seria =",valor)