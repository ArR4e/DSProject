

def moos(suurK,vaikeK,kilogramm):
    karpidearv = 0
    if (suurK*5+vaikeK) < kilogramm:
        return -1
    while True:
        while suurK > 0 and kilogramm >= 5:
            kilogramm = kilogramm - 5 # mitu kilogrammi moosi jääb alles pärast 5kg karbi ära kasutamist
            karpidearv += 1
            suurK -=1
        while vaikeK > 0 and kilogramm > 0: #niikaua kuni on väikeseid karpe rohkem kui 0 ja kilogramme rohkem kui 0, töötab
            kilogramm = kilogramm -1
            karpidearv += 1
            vaikeK -=1
        if vaikeK == 0 and kilogramm > 0: #Kui väiksed karbid saavad otsa aga moosi on veel järel, on vastuseks -1
            karpidearv = -1
        break
    return karpidearv