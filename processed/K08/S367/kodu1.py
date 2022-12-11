from random import sample

def bingo():
    while True:
        bingo = sample(range(1, 11), 3)   
        bingo += sample(range(11, 21), 2)
        if '1' and '2' and'3' not in bingo:
            break
    return bingo
    
        
        