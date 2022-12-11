def moos(s, v, k):
    n = 0
    while k >= 5 and s > 0:
        n += 1
        k -= 5
        s -= 1
    if k == 0:
        return(n)
    else:
        while (k < 5 or s == 0) and k > 0 and v > 0:
            n += 1
            k -= 1
            v -= 1
        if v < 0 or s < 0:
            return(-1)
        elif k == 0:
            return(n)
        else:
            return(-1)