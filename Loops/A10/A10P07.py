r_c = int(input(': '))
i = 1
num = 1
while i<=r_c:
    j = 1
    while j<=r_c:
        if num%2==0:
            print('=', end=' ')
        else:
            print('$', end=' ')
        num+=1
        j+=1
    i+=1
    print()