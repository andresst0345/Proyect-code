num = int (input("Ingresa el numero == "))

mil = (num // 1000 ) % 10
unidades = (num // 100) % 10
dece = (num // 10) % 10
centenas = num % 10

print(f'el numero tiene {mil} Millares ,{unidades} Unidades, {dece} Decenas, {centenas} Centenas ')
