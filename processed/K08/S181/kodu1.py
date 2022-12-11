from random import randrange
import time

def bingo():
    time.sleep(0.1)
    numbrid = []
    for x in range(3):
        numbrid.append(randrange(1,11))
    for y in range(2):
        numbrid.append(randrange(11,21))
    if 1 in numbrid and 2 in numbrid and 3 in numbrid:
        bingo()
    if len(numbrid) != len(list(dict.fromkeys(numbrid))):
        bingo()
    return numbrid

while True:
    print(bingo())