def rek_abs(järjend):
    uus_järjend = []
    for el in järjend:
        if isinstance(el, list): #nii saan teada, et tegemist on järjendiga
            uus_järjend.append(rek_abs(el)) #kutsun välja funktsiooni, et käia läbi sisemise järjendi elemendid
        else:
            uus_järjend.append(abs(el))
    return uus_järjend
            