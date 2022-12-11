def moos(suur, väike, kaal):
    x = 5
    y = 1
    kasutatud_karpe = 0
    while kaal>=x and suur>0:
        kaal-=x
        suur-=1
        kasutatud_karpe+=1
    if väike>=kaal:
        kasutatud_karpe+=y*kaal
        return kasutatud_karpe
    else:
        return -1