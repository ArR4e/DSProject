def auto_hind(alghind, aasta):
    if aasta == 0:
         return alghind
    else:
        while (aasta) > 0:
            alghind = alghind - alghind * 0.2
            aasta -= 1
        return round(alghind,2)
