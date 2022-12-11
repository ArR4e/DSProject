import math

def moos(x,y,z):
    suurkarp = math.floor(z/5)
    v2ikekarp = z - 5*suurkarp
    if x >= suurkarp:
        if y>= v2ikekarp:
            return suurkarp + v2ikekarp
        else:
            return -1
    else:
        if y>= v2ikekarp:
            if suurkarp/x*5 + v2ikekarp < y:
                return x + suurkarp/x*5 + v2ikekarp
            else:
                return -1
        else:
            return -1