def auto_hind(hind, aasta):
    protsent = 20
    if aasta == 0:
        return hind
    else:
        uus_hind = 1 - (protsent/100)
        return round(uus_hind * auto_hind(hind, aasta - 1), 2)
    



print(auto_hind(10000.0, 6), 2)
        