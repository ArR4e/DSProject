def rek_abs(jarjend):
    uus = []
    for el in jarjend:
        if isinstance(el, list):
            uus.append(rek_abs(el))
        else:
            uus.append(abs(el))
    return uus