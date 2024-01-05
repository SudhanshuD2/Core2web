r_c = int(input(': '))
i = 1
a = 1
while i<=r_c:
    j=1
    while j<=r_c:
        if i%2!=0:
            print(a, end=' ')
        else:
            print((a**2), end=' ')
        j+=1
        a+=1
    i+=1
    print()