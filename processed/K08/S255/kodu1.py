from random import sample

def bingo():
    a = sample(range(1, 11), 3)
    while 1 in a and 2 in a and 3 in a:
        a = sample((range(1, 11)), 3)
    b = (sample(range(11, 21), 2)) 
    a.append(b[0])
    a.append(b[1])
    return a
print(bingo())