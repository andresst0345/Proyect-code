a = [-1, 4, 5, 8]

def derv(c):
 n = (len(a))-1
 der = []
 for i in range (n):
  d = a[i] * n 
  der.append(d)
  n = n-1

 return der

k = derv(a)
print(k)

#recursion

def dern(z, y):
 der = []
 for i in range (n):
  d = a[i] * n 
  der.append(d); 
  n = n-1
  



 return der 