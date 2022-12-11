def moos(suur,vaike,kogus):
    karpcount = 0
    algkogus = kogus
    vaba = suur*5 + vaike*1
    if int(kogus) > vaba:
        return(-1)
       

    if kogus//5 > 0:
        if kogus//5 > suur:
            algkogus -= suur*5
            karpcount += suur
        elif kogus//5 == suur:
            algkogus -= suur*5
            karpcount += suur
        elif kogus//5 < suur:
            algkogus -= kogus//5 *5
            karpcount += kogus//5
            
#         algkogus -= (kogus//5 *suur)
#         karpcount += (kogus-algkogus)/5
    
    if algkogus > 0:
        if vaike/algkogus < 1:
            return(-1)
            
        else:
            karpcount += vaike - (vaike-algkogus)
    karpcount = int(karpcount)
    return karpcount
    

print(moos(5, 0, 3))
