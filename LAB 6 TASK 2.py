import math
s = []
dobbie = 1
n = int(input('Число і :'))
for i in range(1,n+1):
     if i%2 == 0:
         sum = 0
         for j in range(1,i+1):
             sum +=1/j
         s.append(sum)
     elif i%2 == 1:
           factorial = 1
           for j in range(1,i+1):
                factorial = math.factorial(i)
                factorial = factorial/2 +3
           s.append(factorial)
for i in range(n):
    if i%2 == 1:
        dobbie *=s[i]
print('Результат={0}.'.format(dobbie))
