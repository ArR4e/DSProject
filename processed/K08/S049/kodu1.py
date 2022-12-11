from random import sample

def bingo():
    a = sample(range(1, 11), 3)
    b = sample(range(11, 21), 2)
    if a == [1, 2, 3]:
        a = sample(range(1, 11), 3)
    else:
        return(a + b)

print(bingo())