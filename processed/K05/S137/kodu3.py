def moos(karpS,karpV,mass):
    arv = 0
    while karpS>0 and mass>=5:
        karpS = karpS - 1
        mass = mass - 5
        arv = arv + 1
    while karpV>0 and mass>0:
        karpV = karpV-1
        mass = mass - 1
        arv = arv + 1
    if mass!=0:
        return -1
    else:
        return arv