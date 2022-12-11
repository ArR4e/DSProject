from math import *
def moos(suur, vaike, kokku):
    x = 5
    vahe = 0
    suuri = 0
    mitux = floor(kokku / 5)
    if mitux < suur:
        vahe = kokku - (mitux * 5)
        suuri = mitux
    else:
        vahe = kokku - (suur * 5)
        suuri = suur
    if vahe > vaike:
        vastus = -1
        return vastus
    elif vahe <= vaike:
        kokku = suuri + vahe
        return kokku
