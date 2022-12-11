def moos(suur, väike, kogus):
    def jagamine(a, b):
        return int(a/b)
    def lahutamine(c, d):
        return c - d
    def liitmine(e, g):
        return e + g
    
    if (suur*5 + väike) < kogus:
        return -1
    elif suur == 0:
        väikeste_arv = lahutamine(kogus, 5*suur)
        if väikeste_arv > kogus:
            return väikeste_arv
        else:
            return -1
    elif väike == 0:
        suurte_arv = jagamine(kogus, 5)
        if suurte_arv != suurte_arv.isfloat():
            return suurte_arv
    elif kogus > 5:
        return(liitmine(suurte_arv, väikeste_arv))
    elif kogus < 5:
        return (kogus/väike)