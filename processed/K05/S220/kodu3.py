def moos(s_karp:int, v_karp:int, kogus:int):
    n = 1
    esialgne = kogus
    mitu_karpi = 0
    mitu_karpi2 = 0
    for i in range(s_karp):
        if (kogus / (5 *n)) >= 1:
            mitu_karpi += 1
            n += 1
        else:
            mitu_karpi += 0
    kogus = kogus - (mitu_karpi * 5)
    for x in range(v_karp):
        if kogus > 0:
            kogus -= 1
            mitu_karpi2 += 1
    kokku = mitu_karpi + mitu_karpi2
    if (mitu_karpi * 5) + mitu_karpi2 < esialgne:
        return -1
    else :
        return kokku

print(moos(1, 2, 10))
            
            
    
    
        
    


