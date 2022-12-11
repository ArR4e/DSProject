def moos(suur,vaike,kogus):
    if kogus > suur*5 + vaike:
        return -1
    
    s = suur
    cratecount = 0
    i = kogus
    while i >= 5 and s:
        i-=5
        cratecount+=1
        s-=1
    
    if i > vaike:
        return -1
    cratecount+=i

    return cratecount