a, b = 1, 100
for i in range(a, b):
    if i%7 == 0 and i%3 != 0:
        print(i, end=' ')
