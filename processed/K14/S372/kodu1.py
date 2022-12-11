def rek_abs(järjend):
    a = []
    for el in järjend:
        if isinstance(el, list) == False:
            if el < 0:
                a.append(el*(-1))
            else:
                a.append(el)
        else:
            a.append(rek_abs(el))
    return a