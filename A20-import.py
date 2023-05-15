path = 'C:/Users/juana/OneDrive/Escritorio/Universidad/Proyect-code/recursos'
file_name = 'employees.txt'
f = []
f = open (path + '/' + file_name)
n = len(file_name)
data = f.readline()
print(data)
f.close()

