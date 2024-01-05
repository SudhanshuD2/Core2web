r_c = int(input(': '))
i = 1
while i<=r_c:
    j = 1
    num = i
    while j<=r_c:
        print(num, end=' ')
        num+=3
        j+=1
    i+=1
    print()