import random

print ('por favor ingresa una palabra palindroma ')
print('\n')
st = input('ingresa la frase o palabra =')
#
def palap (st):
  stc = st
  srv = stc [::-1];srv.split()
  
  if srv == stc :
   c = ('la palabra si corresponde')
  else:
   c = ('la palabra no es palindroma')
  return c
  
print('\n')
print (palap(st))

