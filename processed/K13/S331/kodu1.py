def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    uushind = round(hind*0.8,2)
    return auto_hind(uushind, aasta-1)