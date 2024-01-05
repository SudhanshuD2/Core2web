r_c = int(input(': '))
i = 1
while i <=r_c:
    j = 1
    x = 1
    while j <= r_c:
        if i%2==0:
            print(x, end=' ')
            x+=2
        else:
            print(x+1, end=' ')
            x+=2
        j+=1
    i+=1
    print()