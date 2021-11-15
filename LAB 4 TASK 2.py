# Дійсні числа : a,b,c,d. Чи належать числа
# інтервалу [1;2]&(c;d)


a= float(input('Число  а  : '))
b= float(input('Число  b : '))
c= float(input('Число  c: '))
d= float(input('Число d : '))

if 2>=a>=1 and 2>=b>=1 and d>a>c and d>b>c:
     print( 'true')
else :
     print('false')
