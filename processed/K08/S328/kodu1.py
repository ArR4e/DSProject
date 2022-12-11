from random import sample

def bingo():
    list1 = list(range(1, 11))
    list2 = list(range(11, 21))
    
    num_1 = sample(list1, 3)
    num_2 = sample(list2, 2)
    
    result = num_1 + num_2

    for i in result:
        if 1 in result and 2 in result and 3 in result:
            result = sample(list1, 3) + num_2
            continue
        else:
            break
    return result