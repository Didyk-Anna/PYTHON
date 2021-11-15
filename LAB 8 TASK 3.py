import math as m
def g(i):
    if i==0 :
        return 9
    elif i==1:
        return 35
    else:
        return m.sin(i-1+m.cos(i-2))
s=0
i=float
a=g(7)
b=g(9)
s=s+a+b
print('Значення виразу ={0}'.format(s))
