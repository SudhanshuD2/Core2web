x = int(input("Enter number: "))
a = 0
if x<0:
    while a < 10:
        print(x-1, end=" ")
        x-=1
        a+=1
else:
    while a<10:
        print(-a-1, end=' ')
        a+=1
print()