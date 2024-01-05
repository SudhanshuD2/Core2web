r_c = int(input(': '))
r = 1
od = 1
while r<=r_c:
    c = 1
    while c<=r:
        print(od, end=' ')
        od+=2
        c+=1
    r+=1
    print()