n = 5
for i in range(1, n+1):
    for j in range(0, i):
        print(chr(65 + j) + ' ', end='')
    print()