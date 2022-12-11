from random import sample
def bingo():
    jarg = []
    for i in range(1, 6):
        if i in range(1, 4):
            number = sample(range(1, 11), 1)
        else:
            number = sample(range(11, 21), 1)
        if 1 and 2 in jarg or 2 and 3 in jarg or 1 and 3 in jarg and (number == 1 or 2 or 3):
            i -= 1
            continue
        else:
            jarg.append(number)
    return jarg
print(bingo())