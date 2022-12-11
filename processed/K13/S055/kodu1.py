def auto_hind(hind, aasta):
    if aasta > 0:
        return auto_hind(round(0.8*hind, 2), aasta-1)
    else:
        return hind
