n = 5
for i in range(n):
    num = 1
    for j in range(0, i+1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    print()