def rek_abs(järjend):
    uus = []
    if järjend == []:
        return []
    else:
        for el in järjend:
            if isinstance(el, list):
                uus.append(rek_abs(el))
            else:
                uus.append(abs(el))
        return uus
    