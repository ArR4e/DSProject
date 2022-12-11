def moos(suurKarpArv, vaikeKarpArv,moosKokkuKg):
    karpideArv = 0
    suurKarpKg = 5
    vaikeKarpKg = 1
    
    suurKarpKasutusel = 0
    vaikeKarpKasutusel = 0
    moosTehtudKogusKg = 0
    
    while suurKarpKasutusel < suurKarpArv:
        if (moosTehtudKogusKg + suurKarpKg) <= moosKokkuKg:
            moosTehtudKogusKg += suurKarpKg
            karpideArv += 1
        else:
            break
    while vaikeKarpKasutusel <  vaikeKarpArv:
        if (moosTehtudKogusKg + vaikeKarpKg) <= moosKokkuKg:
            moosTehtudKogusKg += vaikeKarpKg
            karpideArv += 1
            vaikeKarpKasutusel +=1
        else:
            break
        if moosTehtudKogusKg != moosKokkuKg:
            return -1
        else:
            return karpideArv
    