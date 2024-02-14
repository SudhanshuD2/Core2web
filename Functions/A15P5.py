def parent(n):
    def digitCount(num):
        count= 0
        while num!=0:
            num//=10
            count+=1
        return count 
    def evendigitCount(num):
        evencount = 0
        while num!=0:
            dgt = num%10
            if dgt%2 == 0:
                evencount+=1
            num//=10
        return evencount
    def odddigitCount(num):
        oddcount = 0
        while num!=0:
            dgt = num%10
            if dgt%2 != 0:
                oddcount+=1
            num//=10
        return oddcount
    res = [digitCount(n), evendigitCount(n), odddigitCount(n)]
    return res

check = int(input('Enter num: '))
result = parent(check)

print(result)