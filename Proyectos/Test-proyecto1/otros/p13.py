print('Bienvenido por favor ingresa los datos requeridos =) \n')
numero = int(input("Ingrese un número entero mayor a cero: "))
print('\n')
if numero <= 0:
    print("Error: el número ingresado no es mayor a cero.")
else:
    print("Los divisores de", numero, "son:")
    for i in range(1, numero+1):
        if numero % i == 0:
            print(i)