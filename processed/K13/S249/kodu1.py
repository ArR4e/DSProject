def auto_hind(hind, aasta):
    if aasta <= 0:
        return hind
    else:
        uus = hind - hind * 0.2
        return round(auto_hind(round(uus, 2),aasta - 1), 2)
    
print(auto_hind(6788.46, 2))