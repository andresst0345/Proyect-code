# rms
import random
import math as m
a = 20

def rms(a):
  v = [random.randint(-100,100) for vi in range(a) ]
  rms = []
  c = 0
  for ii in v :
      b = (ii) **2
      rms.append(b)
    
  c = sum(rms)
  d = m.sqrt(c)
  return d

print(rms(a))