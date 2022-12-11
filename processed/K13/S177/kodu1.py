def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind, 2)
    else:
        hind = round(hind*0.8, 2)
        aasta -= 1
        return auto_hind(hind, aasta)
vastus = auto_hind(6788.46, 2)
print(vastus)