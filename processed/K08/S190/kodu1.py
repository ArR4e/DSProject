from random import sample

def bingo():
    esimesed_nr = sample(range(1,11),3)
    while True:
        if sum(esimesed_nr) == 6:
            continue
        else:
            break
    x = esimesed_nr[-1]
    y = esimesed_nr[-2]
    z = esimesed_nr[-3]
    
    teised_nr = sample(range(11,21),2)
    
    u = teised_nr[-1]
    v = teised_nr[-2]
    
    return [x,y,z,u,v]

print(bingo())