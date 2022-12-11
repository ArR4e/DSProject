def rek_abs(järjend):
    uusj = []
    if järjend == []:
        return []
    for el in järjend:
        if isinstance(el, list) == False:
            uusj.append(abs(el))
        else:
            uusj.append(rek_abs(el))
        
    else:
        return uusj