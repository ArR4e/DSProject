def auto_hind (hind, aasta):
    if aasta == 0:
        return hind
    else:
        return round(auto_hind(hind - hind*0.2, aasta-1),2)

print (auto_hind(8080.0, 5))