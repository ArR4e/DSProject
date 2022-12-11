def moos(a, b, c):
    x = 0
    jääk = c - (a * 5)
    x += a
    while jääk < 0:
        jääk += 5
        x -= 1
    if jääk > b:
        return -1
    else:
        while jääk != 0:
            x += 1
            jääk -= 1
        return x