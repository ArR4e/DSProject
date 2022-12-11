from random import sample
def bingo():
    while True:
        jarjend = []
        esimesed_num = sample(range(1, 11), 3)
        teised_num = sample(range(11, 21), 2)
        jarjend = esimesed_num + teised_num
        if sum(jarjend[0:3]) != 6:
            break
    return jarjend
print(bingo())
