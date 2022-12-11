def auto_hind(hind, aasta):
    if aasta != 0:
        return auto_hind(round(hind*0.8, 2), aasta-1)
    return round(hind, 2)