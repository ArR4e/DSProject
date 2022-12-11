def auto_hind(hind, aasta):
    if aasta==0:
        return hind
    else:
        return round(0.8* auto_hind(hind, aasta-1),2)
    
#v= auto_hind(8000.0, 5)
