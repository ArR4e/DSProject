import math
def moos(x, y, z):
    Skarp = int(x)
    Vkarp = int(y)
    kogus = int(z)
    Skarpe = math.floor(kogus/5)
    Vkarpe = (kogus-Skarpe*5)
    kokku = Skarpe + Vkarpe
    if kogus > (Skarp*5 + Vkarp) or kogus == 0 or Vkarp < Vkarpe:
        return(-1)
    else:
        return(kokku)
