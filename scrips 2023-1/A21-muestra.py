path = 'C:/Users/juana/OneDrive/Escritorio/Universidad/Proyect-code/recursos'
file_name = 'measurement_data.txt'

with open(path + '/' + file_name) as f :
    data = [float(line) for line in f.readlines()]

n =len(data)
r ,avg = 0 , sum(data) / n

for i in range(n):
    r += (data[i] - avg)**2
r = (r / (n-1))** (1/2)

print(f'la media es {avg}, y la desviacion estandar es {r} \n')


