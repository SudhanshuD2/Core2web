
r_c = int(input('enter number of rows:'))
i = 1
while i<=r_c:
    j = 1
    num = 65
    while j<= r_c:
        print(chr(num), end=" ")
        j+=1
        num+=1
    i+=1
    print()