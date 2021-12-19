numbers=[]
with open('LAB 19 TASK 2.txt', 'r') as file:
    for line in file:
        num = float(line)
        numbers.append(num)
for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers[i] = max(numbers)
with open('task2.txt', 'w') as file2:
    for el in numbers:
        file2.write(str(el) + '\n')
print('найбільше число= {0}'.format((max(numbers))))