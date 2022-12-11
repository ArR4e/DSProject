def rek_abs(järjend):
    uus = []
    for i in järjend:
        if isinstance(i, list):
            uus.append(rek_abs(i))
        else:
            uus.append(abs(i))
    return uus
