def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    else:
        return round(auto_hind((hind / 100) * 80, aasta-1), 2)