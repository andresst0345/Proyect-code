#
n = int (input("ingresa N ="))
m = n
ii = 3
while ii > 0 :
    m = n
    d = 10 ** ii
    q = m // d
    r = m - q * d
    m = r
    ii -= 1
print(m)
