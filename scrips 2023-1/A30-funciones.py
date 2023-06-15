

def f(x):
    if x != 0:
        return 3 **2 + 1 / x + 4
    else :
        return 'inf'

x1 = -10
x2 = 10
inc = 1

while x1 < x2:
    print(x1, f(x1))
    x1 += inc

