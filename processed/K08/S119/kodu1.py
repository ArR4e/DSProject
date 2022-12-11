from random import sample
def bingo():
    while True:
        bingonum = []
        num = sample(range(1, 11), 3)
        num2 = sample(range(11, 21), 2)
        bingonum = num + num2
        summa = bingonum[0] + bingonum[1] + bingonum[2]
        if summa != 6:
            break
    return bingonum
print(bingo())

        