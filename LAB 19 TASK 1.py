
numbers=[]
with open('LAB 19 TASK 1.txt') as file:
    for line in file:
        num=float(line)
        if num<0:
            numbers.append(num)


print(max(numbers))