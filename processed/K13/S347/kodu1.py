def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind,2)
    else:
        return round(auto_hind(float(round(hind, 2) - round(hind,2) * 0.2), aasta-1),2)
print(auto_hind(20000, 9))
    