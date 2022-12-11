from random import randint

def bingo():
    while True:
        num = []
        seen = set()
    
        for i in range(0,3):
            rng = randint(1,10)
            num.append(rng)
            seen.add(rng)
        for i in range(0,2):
            rng = randint(11,20)
            num.append(rng)
            seen.add(rng)
        
        if ((1 in num) and (2 in num) and (3 in num)) or len(seen) != len(num):
            continue
        else:
            return num