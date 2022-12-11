from random import sample

def bingo():
    while True:
        esimesed3 = sample(range(1,11), 3)
        if 1 in esimesed3 and 2 in esimesed3 and 3 in esimesed3:
            continue
        else:
            break
    ülejäänud2 = sample(range(11, 21), 2)
    bingonumbrid = esimesed3 + ülejäänud2
    print(bingonumbrid)

bingo()
    