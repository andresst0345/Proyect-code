contador = 1; a = 0

nacionalidad = input("Ingresa tu nacionalidad: ")
print('\n')
nombre = input("Ingresa tu nombre: ")
print('\n')
edad = int(input("Ingresa tu edad: "))
    
if edad >= 18 and nacionalidad.lower() == "colombiana":
        print("Tienes permitido ejercer el voto en Colombia")
else:
        print("Lo siento, no cumples con los requisitos para votar en Colombia.")
print('\n')
respuesta = input("¿Deseas continuar? (s/n): ")
print('\n')
if respuesta.lower() == "s":
 a = 1

while contador < 10 and a == 1:
    print('---------------\n')
    print(f'persona : {contador} \n')
    nom_ent = input('Ingresa un nombre = ');print('\n')
    edad_ent = input('Ingresa la edad de la persona anterior =');print('\n')
    contador += 1 
else:
     print('gracias por su participacion ')
     
