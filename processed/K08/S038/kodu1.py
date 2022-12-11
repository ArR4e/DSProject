from random import sample

def bingo():
    esimesed = sample(range(1,11),3)
    teised = sample(range(11,21),2)
    lisst = [1,2,3]
    viimane = []
    while True:
        kontroll = all(el in esimesed for el in lisst)
        if kontroll == True:
            esimesed = sample(range(1,11),3)
        else:
            break
    viimane = esimesed + teised
    return viimane

print(bingo())


            

    