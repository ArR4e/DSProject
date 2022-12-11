q = 0
r = 0

def moos(x, y, z):
    q = 0
    r = 0
    
    while z >= 5  and x > 0 :
        z -= 5
        x -= 1
        q += 1
    if y >= z:
        return (q + z)
    else:
        return (-1)
