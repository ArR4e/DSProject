def moos(x, y, z):
    b = 0
    while x > 0 and z >= 5:
        z -= 5
        x-= 1
        b += 1
    while y > 0 and z > 0:
        z -= 1
        y -= 1
        b += 1
    if z != 0:
        b = -1
    return(b)
