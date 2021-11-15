n = list(map(int, input("Введіть цифри: ").split()))


per = 1
while per > 0:
    per = 0
    for i in range(0, len(n)-1):
        if n[i] < n[i+1]:
            n[i+1], n[i] = n[i], n[i+1]
            per += 1

print("Впорядкований масив спадання:")
print(n)
