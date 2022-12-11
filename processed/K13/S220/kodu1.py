def auto_hind(hind, aasta):
    
    if aasta == 0:
        return hind
    else:
        vastus= round(hind * 0.8, 2)
        return auto_hind(vastus, aasta -1)
    


    
    