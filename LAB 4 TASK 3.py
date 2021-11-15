#Трикутник задається координатами своїх вершин на площині: A(x,y)  B(z,k)  C(n,m).
# Визначити, чи є цей трикутник прямокутним.
'''
Довжина  1 сторони      float   - first_side
Довжина  2 сторони      float   - second_side
Довжина  3 сторони      float   - third_side
'''
# 1) Вводимо необхідні дані
import math
x=first_side1= float(input('Координата   1 сторони А : '))
y=first_side2= float(input('Координата   2 сторони А : '))
z=second_side1= float(input('Координата  1 сторони В : '))
k=second_side2= float(input('Координата  2 сторони В : '))
n=third_side1= float(input('Координата  1 сторони С : '))
m=third_side2= float(input('Координата  2 сторони С : '))
# 2) Обчислимо сторони трикутника
a=math.sqrt((z-x)**2+(k-y)**2)
b=math.sqrt((n-z)**2+(m-k)**2)
c=math.sqrt((n-x)**2+(m-y)**2)

if   c**2==(a**2+b**2) or a**2==(b**2+c**2) or b**2==(a**2+c**2) :
     print('Трикутник прямокутний ')
else :
        print('Трикутник не прямокутний')







