# Знайти значення у з системи рівннянь
import math

a= float(input('Число  а  : '))
b= float(input('Число  b : '))
if a > b:
    y=math.cos(a*b)
    print('y=  {0} .'.format(y))
else :
      y=math.log(math.fabs(a))-b
      print('y=  {0} .'.format(y))
