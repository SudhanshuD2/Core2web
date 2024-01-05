r_c = int(input(': '))
r = 1
while r <= r_c:
    c = 1
    while c <= r_c:
        print(f'{c}'+chr(65+r_c-c), end=' ')
        c+=1
    r+=1
    print()