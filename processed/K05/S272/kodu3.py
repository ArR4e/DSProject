def moos(x,y,z):
    karpi = 0
    while x > 0:
        if z-5<0:
            break
        x -= 1
        z -= 5
        karpi += 1
    while y > 0:
        if z-1<0:
            break
        y-=1
        z-=1
        karpi += 1
    if z>0:
        return -1
    else:
        return karpi

moos(3,1,25)