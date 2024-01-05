r_c = int(input(': '))
i = 1
while i <=r_c:
    j = 1
    while j <= r_c:
        if i%2==0:
            print(chr(64+j), end=' ')
        else:
            print(chr(65+r_c-j), end=' ')
        j+=1
    i+=1
    print()