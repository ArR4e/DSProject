def auto_hind(hind, aasta):
    if aasta == 0:
        return float(hind)
    else:
        hind = round(auto_hind(hind, aasta-1)*0.8,2)
        return hind
