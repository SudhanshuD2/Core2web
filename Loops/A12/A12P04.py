r_c = int(input(': '))
i = 1
x = 1
while i<= r_c:
    j = 1
    while j<=r_c:
        print(x, end=' ')
        x+=3
        j+=1
    x-=3
    i+=1
    print()