def moos(suur:int, väike:int, maht:int):
    x = 1
    carp1 = 0
    carp2 = 0
    maht1 = maht
    for i in range(suur):
        if maht/(5*x) >= 1:
            carp1 += 1
            x += 1
        else:
            carp1 += 0
    maht = maht - carp1*5
    for a in range(väike):
        if maht > 0:
            maht -= 1
            carp2 += 1
    if (carp1*5)+carp2 < maht1 :
        return -1
    else:
        return(carp1+carp2)
print(moos(1, 2, 10))