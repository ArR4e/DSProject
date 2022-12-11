def moos(x, y, z):
    i = 0
    while z >= 5 and x >= 1:
        i += 1
        z = z - 5
        x -= 1
    if z <= y:
        i += z
    if z > y:
        return -1
    return i
print(moos(3, 3, 8))