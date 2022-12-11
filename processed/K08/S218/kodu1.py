import random

def bingo():
    järjend = []
    numbrid1 = [1,2,3,4,5,6,7,8,9,10]
    numbrid2 = [11,12,13,14,15,16,17,18,19,20]
    
    while True:
        esimesed = random.sample(numbrid1,3)
        if sum(esimesed)==6:
            continue
        else:
            break
    järjend = järjend + esimesed
    teised = random.sample(numbrid2,2)
    järjend = järjend + teised
    return järjend

print(bingo())