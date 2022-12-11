def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind, 2)
    else:
        return round(auto_hind(hind, aasta-1) * 0.8, 2)

print(auto_hind(10000.0, 6))