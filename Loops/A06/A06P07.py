n = int(input())
count = 0
a = 1
while a <= 200:
    if a%2 == 0:
        count+=1
    if count == n:
        print(f'Even number at position {n} is {a}')
        break
    a+=1