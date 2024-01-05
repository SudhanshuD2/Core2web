r_c = int(input(': '))
r = 1
cnt = 64+r_c
while r<=r_c:
    c = 0
    while c<=r_c-r:
        print(chr(cnt+c), end=' ')
        c += 1
    cnt -= 1
    r+=1
    print()