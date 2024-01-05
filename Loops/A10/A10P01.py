r_c = int(input('Enter row count: '))
r = 1
num = 1
while r<=r_c:
    c = 1
    while c <= r_c:
        print(num**2, end=' ')
        c+=1
        num+=1
    print()
    r+=1
