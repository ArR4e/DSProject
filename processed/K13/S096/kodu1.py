# Kasutatud auto hind rekursiivselt

def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    else:
        return round(auto_hind(hind*0.8, aasta-1),2)
print(f"{auto_hind(6788.46, 2)}")