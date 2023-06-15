import random

a,c,d = random.randint(1,1e3)
b = random.randint(1,1e3)

def suma (a,b):
    return a + b

def dividir(a,b):
    return a / b

def multiplicar(a,b):
    return a * b

def resta(a,b):
    return a - b
 
print(f'{suma}\n {dividir}\n {multiplicar}\n {resta}\n')

