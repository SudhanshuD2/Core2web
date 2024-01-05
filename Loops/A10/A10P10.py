r_c = int(input('enter num of rows:'))
i = 1
while i<=r_c:
    j = r_c
    num = 68
    while j<= r_c and j>0:
        print(chr(num)+str(j), end=' ')
        j-=1
        num-=1
    i+=1
    print()