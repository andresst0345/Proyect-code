#
x0 = 0 
y0 = 0
import math
print("Por favor ingresa las tarifas a definir \n ")

tm = float(input("ingresa la tarifa minima de la carrera ="))
tk = float(input("ingresa el costo por km recorrido = "))
print(" \n")
print("ingresa las coordenadas de la primera parada \n")

x1= float (input("ingresa X de la 1ra coordenada del plano ="))
y1= float (input("ingresa Y de la 1ra coordenada del plano ="))
print(" \n")
print ("ahora ingresa la segunda coordenadas de la segunda parada \n")

x2= float (input("ingresa X de la 2da coordenada del plano ="))
y2= float (input("ingresa Y de la 2da coordenada del plano ="))
print(" \n")
a1 = x1 - x0
a2 = y1 - y0
b1 = x2 - x1
b2 = y2 - y1

dist_t2 = b1 + b2
dist_t1 = a1 + a2

vl_dist =  dist_t1 + dist_t2
cost_dist = vl_dist * tk
dist1t = dist_t1 * tk
dist2t = dist_t2 * tk

if cost_dist <= tm:
    print(f'El costo de su carrera es ==> ',tm)
    print(" \n")
else :
    print("El costo de su carrera tiene un total de ==> \n",cost_dist)
    print(" \n")
    print("su primera parada costo =",dist1t)
    print(" \n")
    print("su segunda parada costo =",dist2t)
    print(" \n")
