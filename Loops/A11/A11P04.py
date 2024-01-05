r_c = int(input(': '))
r = r_c
n = 1
while r>0:
    c = 1
    while c<=r:
        print(n, end=' ')
        c+=1
    n+=1
    r-=1
    print()