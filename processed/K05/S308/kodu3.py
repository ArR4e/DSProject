s=int(input('Sisestage mitu suurt karpi on: '))
v=int(input('Sisestage mitu väikest karpi on: '))
m=int(input('Sisestage mitu kg moosi on: '))
def moos(karp5, karp1, moos):
    karp=0
    while moos >= 5:
        if karp5>=1:
            karp+=1
            moos-=5
        else:
            break
    if moos <= karp1:
        karp=karp+moos
    else:
        karp=(-1)
    return(karp)
print(moos(s,v,m))

        