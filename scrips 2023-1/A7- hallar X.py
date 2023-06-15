import math
from sre_parse import WHITESPACE

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

def calcular_x(a, b):
    x = 1 # Empezamos con un valor inicial de x=1
    while True:
        fx = 7*a / (math.log(3*x + ((8*x**2 - b*x**2) / x)))
        if abs(fx - x) < 0.0001: # Si la diferencia entre fx y x es menor a 0.0001, detenemos el bucle
            break
        else:
            x = fx # Actualizamos el valor de x con fx
    return x

x = calcular_x(a, b)

print("El valor de x es:", x)


