suur = int(input("Sisestage suurte karpide arv:"))
väike = int(input("Sisestage väikeste karpide arv:"))
moos1 = int(input("Sisestage moosi kogus kilogrammides:"))

def moos(suur, väike, moos1):
    purgiluger = 0
    suur = suur
    väike = väike
    moos1 = moos1
    while True:
        if suur > 0 and moos1 >= 5:
            moos1 = moos1 -5
            suur = suur -1
            purgiluger = purgiluger + 1
        elif väike > 0 and moos1 >= 1:
            moos1 = moos1 -1
            väike = väike -1
            purgiluger = purgiluger + 1
        elif suur == 0 and moos1 > 0 or väike == 0 and moos1 > 0:
            return(-1)
            break
        elif suur > 0 and moos1 == 0  or väike > 0 and moos1 == 0:
            return(purgiluger)
            break
        elif moos == 0:
            return(purgiluger)
            break
        
        #vahepeal oli mingi bug sees, aga lihtsustasin kõike ja siis hakkas tööle:)
        
print(moos(suur, väike, moos1))