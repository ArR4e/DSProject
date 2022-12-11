def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    else:
        return auto_hind((round(hind - (hind * 0.2))), aasta -1)
    
print(auto_hind(10000, 5))