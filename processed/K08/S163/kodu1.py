from random import sample

def bingo():
    while True:
        numbrid = sample(range(1, 11), 3) + sample(range(11, 21), 2)
        if  1 in numbrid and  2 in numbrid and  3 in numbrid:
            continue
        else:
            return numbrid
    
print(bingo())