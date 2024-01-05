r_c = int(input(': '))
r = 1
a = 1
while r <= r_c:
    c = 1
    while c <= r_c:
        if c%2!=0:
            print(chr(64+c), end=' ')
        else:
            print(a, end=' ')
        a+=1
        c+=1
    r+=1
    print()