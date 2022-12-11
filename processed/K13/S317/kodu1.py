def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind, 2)
    else:
        return round(auto_hind(round(hind * (1-0.2), 2), aasta-1), 2)