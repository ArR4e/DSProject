def auto_hind(hind, aasta):
    if aasta==0:
        return hind
    else:
        aastas=round(float(hind)*0.8,2)
        return auto_hind(aastas, aasta-1)

print(auto_hind(10000.0, 2))
        
   
    



