def moos(suur, väike, kogus):
    jääk = kogus
    karp = 0
    while True:
        if 0 < suur and (jääk/5 >= 1):
            jääk = jääk - 5
            suur -=  1
            karp += 1
            if jääk == 0:
                return karp
        elif (0 < väike):
            jääk -= 1
            väike -= 1
            karp += 1
            if jääk == 0:
                return karp
        elif kogus == 0:
            return(0)
        else:
            return(-1)

