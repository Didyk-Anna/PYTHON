import random

n=int(input("Введіть кількість рядків матриць A і B:"))
m=int(input("Введіть кількість стовбців матриць A і B:"))
a=[[float(random.randint(0,1))for j in range(m)]for i in range (n)]
b=[[float(random.randint(0,1))for j in range(m)]for i in range (n)]
print(*a, sep = "\n")
x=''
print(x)
print(*b, sep = "\n")

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            a[i][j]= b[i][j]



x=''
print(x)
print(*a, sep = "\n")