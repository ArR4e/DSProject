#1. Kasutatud auto hind rekursiivselt

def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        hind = auto_hind(hind-1, aastad-1)
        uus_hind = hind * (1 - (juurdehindlusprotsent/100))
        return round(uus_hind, 2)

juurdehindlusprotsent = 20
#auto_hind(8000.0, 5)