def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    else:
        uus_hind = hind * 0.8
        return round(auto_hind(uus_hind, aasta-1), 2)
