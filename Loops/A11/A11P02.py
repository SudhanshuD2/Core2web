r_c = int(input(': '))
r = 1
while r<=r_c:
    c = 1
    x = r_c
    while c<=r:
        print(x, end=' ')
        c+=1
        x-=1
    r+=1
    print()