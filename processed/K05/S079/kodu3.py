# 3. Moosi keetmine
# Emma hakkas keetma vaarikamoosi. Tüdrukul olid kasutada 5- ja 1-kilogrammised vaarikakarbid.
# Emmal on moosi tegemisel kombeks kõigepealt kasutada ära kõige suuremad karbid ja seejärel väiksemad.
# Näiteks kui on vaja keeta 8 kg vaarikamoosi, siis võtaks ta kõigepealt ühe suure karbi ning siis kolm väikest karpi.
# Kui plaanitav moosikogus ei mahu karpidesse täpselt ära, siis Emma moosi ei keeda.

# Kirjuta funktsioon moos, mis võtab argumendiks kolm täisarvulist väärtust:

# suurte karpide arvu;
# väikeste karpide arvu;
# keedetava moosi koguse kilogrammides.

# Funktsioon tagastab karpide arvu, mida Emma moosi keetmiseks kasutab. Kui moosikogus antud karpidesse ei mahu,
# tagastab funktsioon arvu -1.

# Näide:

# >>> moos(2, 6, 14)
# 6
# >>> moos(3, 3, 8)
# 4
# >>> moos(1, 2, 10)
# -1
# >>> moos(5, 1, 9)
# -1
# Automaatkontroll. Funktsiooni nimi peab olema moos ja sellel funktsioonil peab olema täpselt kolm argumenti: suurte karpide arv,
# väikeste karpide arv ja moosi kogus. Kõik argumendid on täisarvud. Funktsioon peab tagastama karpide arvu,
# mida tuleb kasutada antud koguse moosi pakendamiseks. Kui ei leidu karpide komplekti, mis moosi täpselt ära mahutaks,
#peab funktsioon tagastama väärtuse -1.

def moos(suur, väike, kg):
    karpide_arv = 0
    suur_karp = suur
    väike_karp = väike
    kaal = kg
    
    if kaal <= 0:
        return karpide_arv
    
    if suur*5 + väike < kaal:
        return -1
    
    while suur_karp > 0:
        karpide_arv += 1
        kaal -= 5
        suur_karp -= 1
        if kaal < 5:
            break
    
    if kaal == 0:
        return karpide_arv 

    if väike_karp >= kaal:
        karpide_arv += kaal
    else:
        return -1
    
    return karpide_arv