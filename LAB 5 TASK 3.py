
import math

x=int(input('Число x: '))

n=int(input('Число n: '))
epsilon=int(input('Число epsilon: '))
suma=0
v=math.log(1-x)
for i in range (1,n+1):
    suma=suma + (x**n)/n
    break
suma=suma*(-1)
if abs(v)-abs(suma)<epsilon:
    print('Рівність справедлива')
else:
    print('Рівність несправедлива')



