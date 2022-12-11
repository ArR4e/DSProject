def moos(suurKarp, vaikeKarp, moosiKogus):
    # vaatab, kas on rohkem moosi kui mahub karpidesse
    if moosiKogus > suurKarp * 5 + vaikeKarp or moosiKogus - moosiKogus // 5 * 5> vaikeKarp:
        return -1
    
    # leiab, mitu suurt karpi saab täita moosiga
    karpideArv = moosiKogus // 5
    if karpideArv > suurKarp:
        karpideArv = suurKarp
    # lahutab originaalsest moosikogusest suurtesse karpidesse mahtunud moosi    
    moosiKogus -= karpideArv * 5
    
    # leiab, mitu väikest karpi läheb ülejäänud moosi jaoks
    if moosiKogus > 0:
        karpideArv += moosiKogus
        
    return karpideArv