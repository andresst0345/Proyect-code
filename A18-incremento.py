a = int(input("Ingresa el valor de inicio ="))
b = int(input("Ingresa valor final ="))
c = int(input("Ingresa valor de Incremento ="))
v = [] ; b += 1 ;a -= 1

for i in range(b):
           if i > a : v.append(i+c)

print(v)


