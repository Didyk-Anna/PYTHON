import math as m
def  function(x,y):
  if x>0  or y>0:
     f = x**3+m.sqrt(x**2+y**4)
  elif x > 0 and y < 0:
     f =  x ** 2 - 2 * x + m.sqrt(x) / (x ** 0.6)
  else : f = m.sin(x*y)
  return f


a = float(input('a:'))
b = float(input('b:'))
v=function(a,b)+function(2,a)+2
print('Значення виразу={0}'.format(v))
