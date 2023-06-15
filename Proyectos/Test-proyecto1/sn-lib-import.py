path = "C:/Users/juana/OneDrive/Escritorio/Universidad/Proyect-code/recursos"
archivo = 'employees.txt'
departamentos = {}

# Leer el archivo y crear el diccionario de departamentos
with open(path + '/' + archivo , encoding= 'utf-8') as t:
    next(t)  # Saltar la primera línea
    data = t.readlines()
    for linea in data:
        nombre, apellido, departamento, salario = linea.strip().split(' ')
        if departamento not in departamentos:
            departamentos[departamento] = []
        departamentos[departamento].append((nombre, apellido, salario))

#Crear las tablas por departamento
for departamento, empleados in departamentos.items():
    # Ordenar los empleados por apellidox
    empleados = sorted(empleados, key=lambda x: x[1])
    tabla = []
    for empleado in empleados:
        tabla.append({'nombre': empleado[0], 'apellido': empleado[1], 'salario': empleado[2]})

    # Mostrar la tabla de manera dividida y ordenada por apellido
    print(f'Tabla de {departamento}')
    print('{:<20} {:<20} {:<10}'.format('Nombre', 'Apellido', 'Salario'))
    print('-' * 50)
    for empleado in tabla:
        print('{:<20} {:<20} {:<10}'.format(empleado['nombre'], empleado['apellido'], empleado['salario']))
    print()

    # Calcular el total anual y mensual de cada departamento
    total_anual = sum(int(e['salario']) * 12 for e in tabla)
    total_mensual = sum(int(e['salario']) for e in tabla)
    print(f'Total anual de {departamento}: {total_anual}')
    print(f'Total mensual de {departamento}: {total_mensual}')

    # Calcular la media de salarios de cada departamento
    media_salarios = total_anual / len(tabla)
    print(f'Media salarial de {departamento}: {media_salarios}')
    print('---')
