r_c = int(input('enter num of rows:'))
i = 1
cap = 65
sma = 97
a = 1
while i<=r_c:
    j = 1
    while j<= r_c:
        if a%2==0:
            print(chr(sma), end=' ')
            sma+=1
            cap+=1
        else:
            print(chr(cap), end=' ')
            cap+=1
            sma+=1
        j+=1
        a+=1
    i+=1
    print()