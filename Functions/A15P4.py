def search_op(lis, s_ele):
    count = 0
    for i in lis:
        if i == s_ele:
            count+=1
        else:
            continue
    return count

li = [1,2,3,3,4,5,3]
search_elem = int(input('Enter search element: '))
return_S = search_op(li, search_elem)
print(f'{search_elem} found in list {return_S} times')
