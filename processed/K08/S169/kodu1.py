import random

def bingo():
    while True:
        list = []
        list += random.sample(range(1,11),3)
        list += random.sample(range(11,21),2)
        if 1 in list and 2 in list and 3 in list:
            list = []
        else:
            return list
        
print(bingo())
