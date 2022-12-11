def auto_hind(hind,aasta):
    if aasta == 0:
        return hind
    else:
        uus_hind = 0.8*(auto_hind(hind, aasta - 1))
        return round(uus_hind,2)