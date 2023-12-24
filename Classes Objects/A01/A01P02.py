def search_count(element):
    list = [13,19,22,29,17,20,26,10,15,11,23,28,12,18,22,24,14,21,30,27,25,10,29,13,17,22,19,11,26,14,15,21]
    c = 0
    for i in list:
        if i==element:
            c+=1
        
    return c

n = int(input("Range-10-30: "))
search = search_count(n)
print(search)
