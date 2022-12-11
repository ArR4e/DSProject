from random import sample
def bingo():
    b = sample(range(11,21), 2)
    a = sample(range(1,11), 3)
    while [1,2,3] in a:
        a = sample(range(1,11), 3)
        if [1,2,3] in a:
            break
    return a + b
print(bingo())
