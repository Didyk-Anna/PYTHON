import math as m
def integral(a,b):
    s=0
    s=s+(b-a)*m.sqrt(4*a+ m.sin ( m.sqrt(a**3)))
    return s
a = float(input('a:'))
b = float(input('b:'))
s=0
v=integral(a,3)
n=integral(a,b)
s=s+v+n
print('Значення виразу ={0}'.format(s))
