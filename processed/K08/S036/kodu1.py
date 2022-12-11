from random import sample
def bingo():
    esimesed = sample(range(1,10),3)
    teised = sample(range(11,20),2)
    while True:
        lst = [1,2,3]
        if esimesed[0] in lst and esimesed[1] in lst and esimesed[2] in lst:
        
            sample(range(1,10),3)
        else:
            break
    return esimesed + teised

print(bingo())