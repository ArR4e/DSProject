def rek_abs(järjend):
    uus_järjend = []
    for i in järjend:
        if isinstance(i, list):
            uus_järjend.append(rek_abs(i))
        else:
            uus_järjend.append(abs(i))
    return uus_järjend