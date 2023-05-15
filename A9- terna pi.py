#pertenece a una terna de pitagoras
a = float(input("ingrese el primer dato = "))
b = float(input("ingrese el segundo dato = "))
c = float(input("ingrese el tercer dato = "))

op = ((a**2) + (b**2)) == c**2

if op == False:
    print("los valores no pertenecen a la terna de pitagoras ==",op)
else :
    print("si pertenece :)")

