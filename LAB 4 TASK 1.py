

 # Обчислити площу трикутника, якщо трикутник задано довжинами сторін.
'''
Довжина  1 сторони      float   - first_side
Довжина  2 сторони      float   - second_side
Довжина  3 сторони      float   - third_side
Напівпериметр           float   - half_perimetr
Площа трикутника   -    float   - area_triangle
'''
import math
# 1) Вводимо необхідні дані


a=first_side= float(input('Довжина  1 сторони  : '))
b=second_side= float(input('Довжина  2 сторони  : '))
c=third_side= float(input('Довжина  3 сторони  : '))
# 2) Обчислимо напівпериметр трикутника
p=(a+b+c)/2
# 3) Обчислення площі трикутника за формулою Герона
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
# 4) Виведемо результат
print('Площа трикутника = {0} .'.format(s))