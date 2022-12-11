def auto_hind(hind,aasta):
    if aasta==0:
        return hind
    else:
        hind=round(0.8*hind,2)
        aasta-=1
        return auto_hind(hind,aasta)
print(auto_hind(10000.0, 6))