def auto_hind(hind,aasta):
    if aasta>=1:
        return auto_hind(round(hind*0.8,2),aasta-1)
    else:
        return round(hind,2)

print(auto_hind(10000.0,5))