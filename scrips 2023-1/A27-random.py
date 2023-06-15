#
import random

n = random.randint(1, 9)
u = [i for i in range(n)]
v = [random.randint(-10,10) for vi in range(n) ]
b = [random.randint(0,1) for bi in range(n)]

print(f'los numeros en rango -10 | 10 con longitud {n} son:{v}\n')
print(f'los numeros en rango 0 | 1 con longitud {n} son:{b}\n')


#%%





