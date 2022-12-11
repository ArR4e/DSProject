def rek_abs(järjend):
    uus_järjend = []
    for el in järjend:
        if isinstance(el, list):
            uus_järjend += [rek_abs(el)]
        else:
            uus_järjend += [abs(el)]
    return uus_järjend
