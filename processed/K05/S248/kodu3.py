def moos(x, y, z):
    if z > x*5+y or z%5-y > 0:
        return -1
    elif z-5*x == 0 or z-y <= 0:
        if x != 0 and z!=0:
            return x
        else:
            return z
    else:
        if z>5*x:
            z -= 5*x
            vkarpe_rohkem = y-z
            vkarpe_vaja = y-vkarpe_rohkem
            return x+vkarpe_vaja
        else:
            skarpe_vaja = z//5
            z -=skarpe_vaja*5
            vkarpe_rohkem = y-z
            vkarpe_vaja = y-vkarpe_rohkem
            return skarpe_vaja+vkarpe_vaja
