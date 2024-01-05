r_c = int(input(': '))
i = 1
a = 1
while i <= r_c:
    j = 1
    while j <= r_c:
        print(a, end=' ')
        a*=2
        j+=1
    i+=1
    print()