def auto_hind(hind, aasta):
    return hind if aasta == 0 else auto_hind(round(hind*0.8,2), aasta-1)

