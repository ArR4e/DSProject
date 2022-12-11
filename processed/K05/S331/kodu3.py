import math
def moos(suuredkarbid, väikesedkarbid, kogus):
    z = math.floor(kogus / 5)
    if z <= suuredkarbid:
        h = int(kogus - z*5)
        if h <= väikesedkarbid:
            return z + h
        else:
            return -1
    elif z >= suuredkarbid:
        h = kogus - suuredkarbid*5
        if h <= väikesedkarbid:
            return suuredkarbid + h
        else:
            return -1
            
    
        

