from random import randint, sample

def bingo():
    while True:
        number1 = [1, 2, 3]
        while number1 == [1, 2, 3] or number1 == [1, 3, 2] or number1 == [3, 1, 2] or number1 == [3, 2, 1] or number1 == [2, 1, 3] or number1 == [2, 3, 1]:
            number1 = sample(range(1, 11), 3)
        number2 = number1 + sample(range(11, 21), 2)
        break
    return number2
print(bingo())