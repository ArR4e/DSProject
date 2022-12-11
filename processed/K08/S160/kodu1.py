from random import sample

def bingo():
    x = sample (range(1,11), 3)
    if x == [1, 2, 3] or x == [3, 2, 1] or x == [1, 3, 2] or x == [2, 3, 1] or x == [2, 1, 3] or x == [3, 1, 2]:
        x = sample (range(4,11), 3)
    y = sample (range(11, 21), 2)
    z = x + y
    return z
    
m = bingo()
print(m)