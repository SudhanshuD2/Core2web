a = int(input('Enter Start: '))
b = int(input('Enter End: '))
for i in range(a, b):
    if 65<=i<=90 or 97<=i<=122:
        ch = chr(i)
        print('The character of ASCII value {} is {}'.format(i, ch))
    else:
        print('Wrong Input')