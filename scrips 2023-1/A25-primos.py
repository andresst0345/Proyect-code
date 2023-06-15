from time  import process_time
tic = process_time()
n = 10013
if n == 2:
    print(f' {n} no es primo')
elif n % 2 == 0:
    print(f' {n} no es primo')
else:
    for i in range (3, int(n/2), 2):
        if i % n == 0:
           break 
        
    
    if i == int(n / 2)-1 :
        print(f'{n} es primo ')
    else:
        print(f' {n} no es primo')

toc = process_time()
print(f'tomo {toc - tic}')

