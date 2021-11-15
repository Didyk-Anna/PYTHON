
x=int(input(' Число n:'))
x_0=1
x_1=1
for i in range( x-1 ):
    el=x_1 +2*(x_0)
    x_0=x_1
    x_1=el
print( 'Число з індекксом  {0}= {1} .'. format(x,el))