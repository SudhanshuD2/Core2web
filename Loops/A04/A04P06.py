a = input('Enter Start: ')
b = input('Enter End: ')
a, b = ord(a), ord(b)
for i in range(a, b+1):
    if 65<=i<=90 or 97<=i<=122:
        ch = chr(i)
        print('ASCII value of {} is {}'.format(ch, i))
    else:
        print('Wrong Input')