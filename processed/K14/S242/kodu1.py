def rek_abs(järjend):
    if isinstance(järjend, list) == False:
        uus_järjend = abs(järjend)
    else:
        uus_järjend = []
        for el in järjend:
            uus_järjend.append(rek_abs(el))
    return uus_järjend
