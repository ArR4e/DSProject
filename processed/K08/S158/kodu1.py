import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

c = random.sample(a,3)
d = random.sample(b,2)

def bingo() :
    return c + d

print(bingo())