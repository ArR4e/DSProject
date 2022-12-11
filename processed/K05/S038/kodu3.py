def moos(suuredKarbid, vaikesedKarbid, kogus):
    if kogus-5*suuredKarbid-vaikesedKarbid>0:
        return(-1)
    else:
        kasutatud = 0
        while kogus-5>=0 and suuredKarbid>0:
            kasutatud += 1
            kogus -= 5
            suuredKarbid -= 1
        while kogus>0 and vaikesedKarbid>0:
            kasutatud +=1
            kogus -= 1
            vaikesedKarbid -=1
        if kogus>0:
            return(-1)
        else:
            return kasutatud
a=int(input("Sisestage suurte karpide arv:"))
b=int(input("Sisestage vaikeste karpide arv:"))
c=int(input("Sisestage keedetava moosi arv kg:"))

print(moos(a,b,c))