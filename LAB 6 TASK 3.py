z = list(map(int, input("Введіть координати вектора : ").split()))

a = float(input('Число на яке множиться вектор :'))
b=[x*a for x in z]
print (b)

