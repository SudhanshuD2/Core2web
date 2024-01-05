r_c = int(input(': '))
i = 1
while i <= r_c:
    j = 1
    while j <= r_c:
        if (i+j)%2==0:
            print('$', end=' ')
        else:
            print('=', end=' ')
        j+=1
    i+=1
    print()