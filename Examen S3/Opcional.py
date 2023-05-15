# fibbonnaci
a = int(input('ingresa el numero de terminos a mostrar = '))
print('\n')

def fibci(n):
  a, b = 0, 1
  fb = []
  for i in range(2, n):
    c = a + b
    fb.append(c)
    a = b
    b = c

  return fb

c = fibci(a)
print(c)