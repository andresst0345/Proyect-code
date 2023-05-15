# db
import  math as m
vref = float(input('Ingresa el valor de referencia '))

def dbl(val):
    db = 10 * m.log10(val**2)

    return db


def ldb(db):
    val = m.sqrt(10**(db/10))

    return val

x = dbl(vref)
y = ldb(x)

print('\n')
print(f'el valor de referencia fue {vref} y su transformacion a db es =',(x),'\n')
print('\n')
print(f'su retorno a un valor de referencia es =',(y),'\n')