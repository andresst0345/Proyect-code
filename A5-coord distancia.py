import math
print("ingresa las primeras coordenadas")

x1= float (input("ingresa X de la 1ra coordenada del plano ="))
y1= float (input("ingresa Y de la 1ra coordenada del plano ="))

print ("ahora ingresa la segunda coordenada")

x2= float (input("ingresa X de la 2da coordenada del plano ="))
y2= float (input("ingresa Y de la 2da coordenada del plano ="))

l1 = x2-x1
l2 = y2-y1

h = math.sqrt((l1**2)+(l2**2))
#print("la distancia entre las dos coordenadas es ==>",h)

dr = l1 + l2

tr = (dr / 1e3) *dr
