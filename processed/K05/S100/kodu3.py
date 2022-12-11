def moos(a, b, c):
    kokku = 0
    
    while True:
        if c >= 5 and a > 0:
            c -= 5
            a -= 1
            kokku += 1
        elif c >= 1 and b > 0:
            c -= 1
            b -= 1
            kokku += 1
        if c == 0:
            return kokku
        
        if not (c >= 5 and a > 0) and not(c >= 1 and b > 0):
            return -1
