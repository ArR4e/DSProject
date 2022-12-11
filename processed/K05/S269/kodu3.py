def moos(s, v, m):
    if 5*s + v < m or m%5 > v:
        return -1
    else:
        karpe = 0
        while s > 0 and m >= 5:
            m -= 5
            s -= 1
            karpe += 1
        karpe += m
        return karpe
            
        