def moos(suur, vaike, kg):
    karpe=0
    #Kasutab võimalikult palju suuri karpe kui neid on
    while kg >= 5 and suur != 0:
        karpe+=1
        suur-=1
        kg-=5
    #Kasuta võimalikult palju väikseid karpe kui neid on
    while kg >= 1 and vaike != 0:
        karpe+=1
        vaike-=1
        kg-=1
    #Kui moosi jääb pärast karpidesse panemist alles, siis tulemus -1
    if kg != 0:
        karpe = -1
    return karpe