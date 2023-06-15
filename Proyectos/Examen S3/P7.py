#numeros primos 

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
primos = []

for i in range(2, numero):
    if es_primo(i):
        primos.append(i)

print('\n')
tnp = sum(primos)
print(f"Los números primos menores a {numero} son: {primos}",'\n')
print(f'la suma de los numeros primos es ={tnp} ')

















