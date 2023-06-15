from time  import process_time
tic = process_time()
import pandas as pd
path = "C:/Users/juana/OneDrive/Escritorio/Universidad/Proyect-code/recursos"
archivo = 'employees.txt'
with open(path + '/' + archivo , encoding= 'utf-8') as t:
    data = t.readlines()

# diccionario vacío para cada departamento

departamentos = {}
for line in data[1:]:
    nombre, apellido, departamento, salario = line.strip().split()
    salario = int(salario)
    if departamento not in departamentos:
        departamentos[departamento] = {"nombre":[], "apellido":[], "salario":[]}
    departamentos[departamento]["nombre"].append(nombre)
    departamentos[departamento]["apellido"].append(apellido)
    departamentos[departamento]["salario"].append(salario)

# Crear una tabla para cada departamento y guardarla en un archivo csv
for departamento, empleados in departamentos.items():
    df = pd.DataFrame(empleados)
    df.to_csv(f"{departamento}.csv", index=False, sep=';', header=True)

toc = process_time()
print(f'tomo {toc - tic}')
