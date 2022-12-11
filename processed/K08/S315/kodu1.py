from random import sample

def bingo():
    while True:
        üks = 0
        kaks = 0
        kolm = 0
        list1 = sample(range(1, 11), 3)
        list2 = sample(range(11, 21), 2)
        bingo = list1 + list2
        for i in range(len(bingo)):
            if bingo [i] == 1:
                üks = 1
            elif bingo [i] == 2:
                kaks = 2
            elif bingo [i] == 3:
                kolm = 3
                
        if üks == 1 and kaks == 2 and kolm == 3:
            continue
        else:
            break
            
    return bingo
    