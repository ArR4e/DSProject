def auto_hind(hind,aasta):
    if aasta==0:
        return hind
    else:
        return round(auto_hind(0.8*hind,aasta-1),2)