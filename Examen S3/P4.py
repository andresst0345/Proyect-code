#sin(x)
import  math as m

x = int(input(f'ingresa el valor de x del sin(x) = '))
print('\n')
n = int (input(f'Ingresa el valor de N en la ecuacion ='))

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact



def sin(n, x):
   
    aprox = 0
    for n in range(n):
        sig = (-1) ** n
        num = x ** (2*n + 1)
        den = factorial(2*n + 1)
        termino = sig * num / den
        aprox += termino
    
    return aprox

aproximacion = sin(n, x)
print('\n')
print(f"La aproximación de sen({x}) con {n} términos es: {aproximacion}")
print('\n')