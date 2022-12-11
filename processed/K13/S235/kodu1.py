def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    if aasta > 0:
        hind = hind*0.8
        hind = round(hind, 2)
        return auto_hind(hind, aasta-1)