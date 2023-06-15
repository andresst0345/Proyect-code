from time  import process_time
import pandas as pd

tic = process_time()
path = "C:/Users/juana/OneDrive/Escritorio/Universidad/Proyect-code/recursos"
archivo = 'employees.txt'
with open(path + '/' + archivo , encoding= 'utf-8') as t:
    data = t.readlines()
#
departamentos = {}
for line in data[1:]:
    nombre, apellido, departamento, salario = line.strip().split()
    salario = int(salario)
    if departamento not in departamentos:
        departamentos[departamento] = {"nombre":[], "apellido":[], "salario":[]}
    departamentos[departamento]["nombre"].append(nombre)
    departamentos[departamento]["apellido"].append(apellido)
    departamentos[departamento]["salario"].append(salario)

# 
for departamento, empleados in departamentos.items():
    df = pd.DataFrame(empleados)
    df.to_csv(f"{departamento}.csv", index=False, sep=';', header=True)

    #
    total_mensual = sum(empleados["salario"])
    num_empleados = len(empleados["salario"])
    total_anual = total_mensual*12
    media = sum(empleados["salario"]) / len(empleados["salario"])
    media_sal_emp = total_anual / num_empleados
    print(f"\n{departamento}:\n{'-' * 25}\nTotal anual: {total_anual}\nTotal mensual: {total_mensual:.2f}\n "+\
          f"Media: {media:.2f}\n Total de empleados: {num_empleados}\n Total por empleado: {media_sal_emp}\n")

toc = process_time()
print(f'Tomo {toc - tic} s')