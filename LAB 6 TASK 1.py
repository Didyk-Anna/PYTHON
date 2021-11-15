import statistics

z = list(map(int, input("Введіть числа : ").split()))

gm=statistics.geometric_mean(z)
print(' Середнє геометричне ={0}.'. format(gm))
