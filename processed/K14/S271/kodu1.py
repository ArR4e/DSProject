def rek_abs(jarjend):
    uus = []
    for x in jarjend:
        if isinstance(x, list):
            uus.append(rek_abs(x))
        else:
            uus.append(abs(x))
    return uus