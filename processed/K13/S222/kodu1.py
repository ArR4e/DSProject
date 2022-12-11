def auto_hind(hind,aasta):
    if aasta > 0:
        return auto_hind(hind*0.8,aasta-1)
    else:
        return round(hind,2)