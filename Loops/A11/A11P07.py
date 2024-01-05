r_c = int(input(': '))
r = 1
z = 1
while r<=r_c:
    x = z
    c = 1
    while c<=r:
        print(x, end=' ')
        c+=1
        z = x
        x+=1
    r+=1
    print()