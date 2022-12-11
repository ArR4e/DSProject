from random import sample
def bingo():
    x = sample(range(1,11),3) + sample(range(12,21),2)
    return x
print(bingo())
