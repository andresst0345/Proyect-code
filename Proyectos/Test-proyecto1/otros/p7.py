import math

longitud = float(input("Ingresa la longitud de la línea en cm: "))
area_triangulo = (math.sqrt(3) / 4) * longitud ** 2
#
area_cuadrado = longitud ** 2
#
radio = longitud / 2
#
area_circulo = math.pi * radio ** 2
#
print('------------------\n')
print("El área del triángulo equilátero es:", round(area_triangulo, 2), "cm^2 \n")
print("El área del cuadrado es:", round(area_cuadrado, 2), "cm^2 \n")
print("El área del círculo es:", round(area_circulo, 2), "cm^2 \n")
