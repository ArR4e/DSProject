def auto_hind(hind,aasta):
    if aasta == 0:
        return hind
    else:
        return round(auto_hind(round((hind*0.8), 2),aasta-1) ,2)