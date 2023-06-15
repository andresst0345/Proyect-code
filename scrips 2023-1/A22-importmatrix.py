path = 'C:/Users/juana/OneDrive/Escritorio/Universidad/Proyect-code/recursos'
file_name = '1000_digits_number.txt'

with open(path + '/' + file_name) as f :
    data = f.readline

n = len(data)

print(n)

