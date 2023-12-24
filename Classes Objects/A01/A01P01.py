#An array of factorial elements
import array as arr
def factorial(a):
    result = arr.array('i', [])
    facto = 1
    for i in range(1, a+1):
        facto *= i
        result.append(facto)
    return result

n = int(input('Enter: '))
if n >0:
    abc = factorial(n)
    print(abc)
else:
    raise ValueError(f'Input must be greater than 0, provided {n}')