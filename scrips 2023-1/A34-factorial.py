import random
#
print(f'seleciona el metodo a implementar.')
print('\n')
print(f'1. eliminar los valores sobresalientes')
print(f'2. reemplazar por el umbral')
print(f'3. reemplazar por 0')
print('\n')
lim = int(input(f'Ingresa el umbral =='))
print('\n')
selc = input(f'ingresa tu eleccion == ')
#
vec = [random.randint(1,500) for vi in range(16)]
#
match selc :
    
   case "1" :
      fil1 = []
      for i in  vec:
         if i <= lim :
          fil1.append(i)
      print(f'el resultado de tu elecion es = ',(fil1))
      
   
   case "2":
      fil2 = []
      fil2 = vec
      for ii in range(len(fil2)):
         if fil2[ii] >= lim :
            fil2[ii] = lim 
      print(f'el resultado de tu elecion es = ',(fil2))

   case "3":
      fil3 = []
      fil3 = vec
      for iii in range(len(fil3)):
         if fil3[iii] >= lim :
            fil3[iii] = 0
      print(f'el resultado de tu elecion es = ',(fil3))


print('\n')
print(f'el vector usado fue ==>')
print(vec)