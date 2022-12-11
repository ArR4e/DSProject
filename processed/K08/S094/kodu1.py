from random import sample


def bingo():
    while True:
        # kokku 5 arvu, teeme 2 eraldi loosi.
        # vahemikus 1-10
        loosime_3 = sample(range(1,11), 3)
        
        # vahemikus 11-20
        loosime_2 = sample(range(11,21), 2)
        
        loosinumbrid = loosime_3 + loosime_2
        
        # kontroll et ei oleks jarjest 1,2,3.
        if "1" and "2" and "3" in loosinumbrid:
            continue
        else:
            break
    return loosinumbrid
