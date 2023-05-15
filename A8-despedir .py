nom = input("ingresa tu nombre por favor ==")
print("Ingresa tu genero opresor ",\
      '1.Masculino',
      '2.Femenino',
      '3.Binario Hexadecimal',
      '4.Prefiero no decir', sep='\n')

gen = input("ingresa la opcion escogida == ")

if gen == 1:
    print(f'Hola{nom}, Te informamos que has sido despedido')
elif gen == 2:
    print(f'Hola{nom}, Te informamos que has sido despedida')
elif gen == 3:
    print(f'Hola{nom}, Te informamos que has sido despedide')
elif gen == 4:
    print(f'Hola{nom}, Te informamos que ya no haces parte de la compañia')
else :print(f'Hola{nom}, Te informamos que has sido despedido')
