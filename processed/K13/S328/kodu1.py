def auto_hind(hind, aasta):
    if aasta > 0:
        new_hind = round(hind * 0.8, 2)
        return auto_hind(new_hind, aasta - 1)
    else:
        return hind
    
print(auto_hind(10000.0, 1))