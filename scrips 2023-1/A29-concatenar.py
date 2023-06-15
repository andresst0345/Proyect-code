from time import process_time
 
#
m = 10
n = int(1000)
for i1 in range(m):
    tic = process_time()
    a = []
    for i in range(n):
        a.append(0)
    toc = process_time()
    t = toc - tic ; t1= [] 
    t1.append(t)
print(f'tiempo promedio append = {(sum(t1)/len(t1))} s')
#

for i2 in range(m):

    tic = process_time()
    a = []
    for i in range(n):
        a += [0]
    toc = process_time()
print(f'+=[0] tomó {toc - tic} s')
#

tic = process_time()
a = [0 for i in range(n)]
toc = process_time()
print(f'list_comp tomó {toc - tic} s')
 
tic = process_time()
a = [0] * n
toc = process_time()
print(f'replication tomó {toc - tic} s')