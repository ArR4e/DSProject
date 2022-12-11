def moos(x, y, z):
    karbid = 0
    while x>0 and z//5>=1:
        karbid += 1
        z -= 5
        x -= 1
    if z<=y:
        karbid += z
        return(karbid)
    else:
        return(-1)
