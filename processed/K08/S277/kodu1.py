from random import sample

def bingo():
    while True:
        esimesed = sample(range(1, 11), 3)
        teised = sample(range(11, 21), 2)
        bingonr = esimesed + teised
        
        if (1 in bingonr) and (2 in bingonr) and (3 in bingonr):
            continue
        else:
            return bingonr

print(bingo())
    
    

