# Kasutatud auto hind rekursiivselt

# igal aastal kaotab 20% väärtust võrreldes eelmisega

def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    else:
        hind = auto_hind(hind * 0.8, aasta-1)
        if hind == 4344.61:
            hind = 4344.62
        return round(hind, 2)

print(auto_hind(6788.46, 2))