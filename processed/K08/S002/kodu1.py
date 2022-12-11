from random import sample

def bingo():
    return sample(range(1,11),3)+sample(range(11,21),2)

print(bingo())