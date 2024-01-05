r_c = int(input(': '))
r = 1
while r<=r_c:
    c = r_c
    while c>r_c-r:
        print(chr(c+64), end=' ')
        c-=1
    r+=1
    print()