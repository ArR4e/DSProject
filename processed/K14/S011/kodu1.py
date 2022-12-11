def rek_abs(järjend):
    uus = []
    if järjend == []:
        return uus
    for el in järjend:
        if isinstance(el, list) is True:
            uus.append(rek_abs(el))
        else:
            if el < 0:
                uus.append(-el)
            else:
                uus.append(el)
    return uus
    
                