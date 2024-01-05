a = int(input(': '))
cnt = 1
i = 1
while i<=a:
    j = 1
    while j<=i and cnt>0:
        print(cnt, end=' ')
        cnt+=1
        j+=1
    i+=1
    print()