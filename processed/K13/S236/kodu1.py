#1. Kasutatud auto hind rekursiivselt

def auto_hind(hind, aastad):
    if aastad == 0:
        return round(hind, 2)
    else:
        return auto_hind(hind * 0.8, aastad - 1)
