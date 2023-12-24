def parent(a):
    def digitCount():
        count = 0
        for num in li:
            if num ==0:
                count+=1
            else:
                curr = num
                if curr<0:
                    curr*=-1
                
                while curr >0:
                    curr//=10
                    count +=1
        return count
    def evendigitCount():
        evencount = 0
        for num in li:
            if num ==0:
                evencount+=1
            else:
                if num%2==0:
                    evencount+=1
                else:
                    pass
                curr = num
                if curr<0:
                    curr*=-1
                while curr >0:
                    curr//=10
                    if curr%2 ==0:
                        evencount+=1
        return evencount
    def odddigitCount():
        oddcount = 0
        for num in li:
            if num == 0:
                pass
            else:
                if num%2==0:
                    pass
                else:
                    oddcount+=1
                curr = num
                if curr<0:
                    curr*=-1
                while curr>0:
                    curr//=10
                    if curr%2!=0:
                        oddcount+=1
        return oddcount
    if a == 1:
        return digitCount()
    elif a == 2:
        return evendigitCount()
    elif a == 3:
        return odddigitCount()
    else:
        raise ValueError('Choose between 1-3')

    

#total = int(input('Total elements: '))
li = [25, 0, 15588]
'''put = input('space seprated: ').split()
if len(put) == total:
    for ele in put:
        li.append(int(ele))
'''
n = int(input('choose function:\n1.DigitCount\t2.EvenDigitCount\t3.OddDigitCount\n: '))
pa = parent(n)
print(pa)
