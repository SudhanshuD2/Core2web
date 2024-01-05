x = int(input('Eneter num of rows: '))
a = 1
i = 1
ad = 1
while i<=x:
    j = 1
    while j <=x:
        a+=ad
        print(a, end=' ')
        j+=1
        ad+=2
    i+=1
    print()