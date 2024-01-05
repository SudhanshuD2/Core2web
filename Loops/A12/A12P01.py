r_c = int(input('Num of rows: '))
i = 1
s = 0
ad = 3
while i <= r_c:
    c = 1
    while c<=r_c:
        print(s, end=' ')
        s+=ad
        ad+=2
        c+=1
    i += 1
    print()