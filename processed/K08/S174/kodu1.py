from random import sample

def bingo():
    while True:
        bingo_kolm = sample(range(1, 11), 3)
        bingo_kaks = sample(range(11, 21), 2)
        if sum(bingo_kolm) != 6:
            tulemusjärjend = bingo_kolm + bingo_kaks
            return tulemusjärjend
            
        
#print(bingo())

            
    