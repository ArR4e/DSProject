def bingo():
    l = sample(range(1, 11), 3)
    while 1 in l and 2 in l and 3 in l:
        l = sample(range(1, 11), 3)
    l1 = sample(range(11,21), 2)
    l2 = l + l1
    
    return l2

from random import sample
print(bingo())
