def rek_abs(järjend):
    uus = []
    for el in järjend:
        if not isinstance(el, list):
            uus.append(abs(el))
        else:
            uus.append(rek_abs(el))
    
    return uus
            