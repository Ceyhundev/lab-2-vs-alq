from math import *
from random import *
n=int(input("n="))
a=[0]*n
for i in range(n):
        a[i]= randint(5,54)
p=0
q=0
for i in range(n):
        if a[i] % 5 == 0   :
            q+=1
            p=p+a[i]
s=p/q
print(s)