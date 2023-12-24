x = 1
count = 0
while x <= 30:
    if x%2==1:
        count+=1
    
    if count == 7:
        print(f'7th odd number is {x}')
        break
    x += 1
