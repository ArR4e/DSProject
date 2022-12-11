from random import sample

def bingo():
    while True:
        numbers = sample(range(1, 11), 3)
        if sum(numbers) == 6:
            continue
        else:
            numbers += sample(range(11, 21), 2)
            break
    return numbers