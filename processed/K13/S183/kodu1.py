def auto_hind(hind, aasta):
    if int(aasta) == 0:
        return round(float(hind), 2)
    else:
        uus_hind = round(float(hind) * 0.8, 2)
        return auto_hind(uus_hind, aasta-1)

      