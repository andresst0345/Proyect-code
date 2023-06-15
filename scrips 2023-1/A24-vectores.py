from time  import process_time
tic = process_time()
v0 = []
v1 = []
v2 = []
n = 128
a = 0 ; b = 1
for i in range(n):
    v0.append(a)
    v1.append(b)


for ii in range(int (n/2)):
    v2.append(a)
    v2.append(b)
    
toc = process_time()
print(f'tomo {toc - tic}')
print(len(v0))
print(len(v1))
print(len(v2))