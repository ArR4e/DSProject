def moos(suurkarp, väikekarp, moosihulk):
    
    suurkarpmaht = 5
    väikekarpmaht = 1
    suurtekmaht = suurkarp * suurkarpmaht
    väikestekmaht = väikekarp * väikekarpmaht

    skarphulk = int(moosihulk / suurkarpmaht)
    vkarphulk = moosihulk % suurkarpmaht
    
    karphulk = skarphulk + vkarphulk
    
    if moosihulk % suurkarpmaht < 1:
        if moosihulk > (suurtekmaht + väikestekmaht):
            return( -1)
        else:
            return (karphulk)
    else:
        if moosihulk > (suurtekmaht + väikestekmaht):
            return (-1)
        else:
            return (karphulk)

suurkarp = int(input("Sisesta suurte karpide arv: "))
väikekarp = int(input("Sisesta väiksemate karpide arv: "))
moosihulk = int(input("Sisesta keedetava moosi hulk: "))

moos(suurkarp, väikekarp, moosihulk)
   
    