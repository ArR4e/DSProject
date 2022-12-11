import random

def bingo():
    järj = random.sample(range(1, 11), 5)
    valejärj = [1, 2, 3]
    while järj[0] == 1 or järj[1] == 1 or järj[2] == 1 and järj[1] == 2 or järj[2] == 2 or järj[3] == 2 and järj[2] == 3 or järj[3] == 3 or järj[4] == 3:
        järj = random.sample(range(1, 11), 5)
    
    print(järj)
       
bingo()   