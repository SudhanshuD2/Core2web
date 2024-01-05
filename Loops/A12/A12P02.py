r_c = int(input(': '))
i = 1
a = 65
while i <= r_c:
    j = 1
    while j <= r_c:
        print(chr(a), end=' ')
        a+=1
        j+=1
    a-=1
    i+=1
    print()