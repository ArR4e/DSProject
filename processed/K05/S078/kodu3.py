def moos(x, y, z):
    karbid = 0
    kalu = 0
    while z > 0:
        if z- 5 >= 0 and x > 0:
            z -= 5
            x -= 1
            karbid += 1
        elif z - 1 >= 0 and y > 0:
            z -= 1
            y -= 1
            karbid += 1
        else:
            return -1
    return karbid