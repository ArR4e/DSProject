from random import sample

def bingo ():
    i = 0
    while i <= 1000:
        bingo=[]
        
        esimesed = sample(range(1, 11), 3)
        teised = sample(range(11, 21), 2)
    
        for elemendid in esimesed:
            bingo.append(elemendid)
        for elemendid2 in teised:
            bingo.append(elemendid2)
            
        if 1 and 2 and 3 in bingo:
            continue
        
        i +=1
    return bingo

print (bingo())
        