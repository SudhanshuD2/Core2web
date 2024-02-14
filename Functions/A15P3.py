def facto(li):
    res = []
    for n in li:
        fac = 1
        for i in range(1,n+1):
            fac *= i
        res.append(fac)
    return res

arr = [1,2,3,4,5]
ret_factorial = facto(arr)
print(ret_factorial)
