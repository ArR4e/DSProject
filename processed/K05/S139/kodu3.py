def moos (s, v, m):
    karpe = 0
    while m >= 5 and s != 0: 
        m -= 5
        karpe += 1
        s -= 1
    else:
        while m > 0 and v != 0:
            m -= 1
            karpe += 1
            v -= 1
            
        if v < m:
            return -1                
        else:
            return karpe           

moos(3, 3, 8)