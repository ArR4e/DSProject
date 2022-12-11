from random import sample

def bingo():
    while True:
        numbers = sample(range(1, 11), 3)
        if 1 in numbers and 2 in numbers and 3 in numbers:
            continue
        break
    numbers += sample(range(11, 21), 2)
    return numbers