def  rek_abs(järjend):
    a = []
    for element in järjend:
        if isinstance(element, list):
            a.append(rek_abs(element))
        else:
            a.append(abs(element))
    return a