def rek_abs(järjend):
    uus = []
    n = 0
    if isinstance(järjend, list) == True:
        for el in järjend:
            uus.append(rek_abs(el))
    else:
        return abs(järjend)
        
    return uus