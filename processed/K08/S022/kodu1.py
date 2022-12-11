from random import sample

def bingo():
    a = []
    while True:
        b = sample(range(1, 11), 3)
        if b[0] + b[1] + b[2] == 6:
            continue
        else:
            break
    a = a + b
    c = sample(range(11, 21), 2)
    a = a + c
    return (a)
  

print(bingo())
