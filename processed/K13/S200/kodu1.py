def auto_hind(hind,aasta):
    hind = round(hind,2)
    if aasta == 0:
        return round(hind,2)
    elif aasta > 0:
        return auto_hind(round(hind*0.8,2),aasta-1)
    
print(auto_hind(6788.46, 2))