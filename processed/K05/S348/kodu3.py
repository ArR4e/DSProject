def moos(a, b, c):
    arv = 0
    
    while (a > 0 and c > 4):
        c -= 5
        a -= 1
        arv += 1
        
    while (b > 0 and c > 0):
        c -= 1
        b -= 1
        arv += 1
        
    if c != 0:
        arv = -1
        
    return(arv)


