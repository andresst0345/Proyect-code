


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def suma_resta(h, j):
    return [suma(h, j), resta(j, h)]

x = 45
y = -39
w = suma(x, y)
u = resta(y, x)
print(w,u,'\n',suma_resta(x,y))