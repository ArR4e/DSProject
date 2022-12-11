from random import sample
from time import sleep

def bingo():
    while True:
        esimesed = sample(range(1, 11), 3)
        viimased = sample(range(11, 21), 2)
        numbrid = esimesed + viimased
        if 1 in numbrid and 2 in numbrid and 3 in numbrid:
            print("ERROR")
            continue
        break
    return numbrid

while True:
    print(bingo())
    sleep(0.1)
