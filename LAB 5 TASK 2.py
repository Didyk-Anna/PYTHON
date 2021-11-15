n = int(input('Введiть число: '))
N = 0

while n > 0:
    n, c = divmod(n, 10)
    if c == 0:
        N += 1

print('Кiлькiсть нулiв: {0}.'.format(N) )