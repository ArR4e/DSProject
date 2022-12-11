def moos(x,y,z):
    karp=0
    while x or y != 0 or z == 0:
        if z >= 5 and x > 0:
            karp+=1
            z-=5
            x-=1
            continue
        elif z != 0 and y > 0:
            karp+=1
            z-=1
            y-=1
            continue
        elif z!=0:
            return -1
        else:
            return karp
    else:
        return -1

