from random import sample


def bingo():
    x = sample(range(1, 11), 3)
    while [1, 2, 3] in x:
         x = sample(range(1, 11), 3)
#     if sum(x) == 6:
#         continue
    y = sample(range(11, 21), 2)
    m = x + y
    return m

    
print(bingo())
