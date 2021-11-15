import math

a=float(input('Число а: '))
n=int(input('Число n: '))
sum = math.log(math.fabs(a **1))
for i in range(n):
    sum=sum+math.log(math.fabs(a**(n+1)))
    a = math.log(math.fabs(a ** (n + 1)))
    a =math.log(math.fabs(a ** (n +2)))

print ('sum={0}.'.format(a))
