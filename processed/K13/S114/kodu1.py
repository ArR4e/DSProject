def auto_hind(hind,aasta):
    if aasta == 0:
        return hind
    else:
        hind = round(hind-(hind*0.2),2)
        return(auto_hind(hind,aasta-1))
