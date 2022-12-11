import math
def moos(suur, väike, kg):
    Suur = 5
    Väike = 1
    if (suur * Suur + väike * Väike) >= kg:
        ssuur = kg/Suur
        suurtearv = math.floor(ssuur)
        if suurtearv > suur:
            suurtearv = suur
            kg -= suurtearv*5
            väikestearv = kg
            return (suurtearv + väikestearv)

        kg -= suurtearv*5
        väikestearv = 0
        if väike >= kg:
            if kg > 4:
                väikestearv = 5
            elif kg > 3:
                väikestearv = 4
            elif kg > 2:
                väikestearv = 3
            elif kg > 1:
                väikestearv = 2
            elif kg > 0:
                väikestearv = 1
        else:
            return -1
        return (suurtearv + väikestearv)
    else:
        return -1
