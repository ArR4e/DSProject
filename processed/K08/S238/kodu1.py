from random import sample

def bingo():
    a = []
    b = []
    a = sample(range(1,10),3)

    while True:
        count = 0
        for el in a:
            if el == 1:
                count += 1
            if el == 2:
                count += 1
            if el == 3:
                count += 1
        if count == 3:
            a = sample(range(1,11),3)
        if count < 3:
            break
        
    b = sample(range(11,21),2)
    c = a+b
    return c
    


print(bingo())