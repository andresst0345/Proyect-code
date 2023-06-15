import random

a = int (input('valor A ='))
b = int (input('valor B ='))

k = random.randint(a,b )
u = [i for i in range(k)]
y = [random.randint(1,8) for vi in range(k)]
x = [random.randint(1,6) for bi in range(k)]
z = [random.randint(1,8) for bi in range(k)]
xs = len(x);zs = len(z); ys = len(y)


#%% suma vec A
if xs == ys:
    mat = []
    for i in range(zs):
        mat.append(x[i] + y[i])
        print(mat)
else :
    print('no tiene la misma longitud de elementos')

#%% suma B


