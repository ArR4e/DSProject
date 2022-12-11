def rek_abs(järjend):
    absJärjend = []
    for el in järjend:
        if isinstance(el, list):
            absJärjend.append(rek_abs(el))
        else:
            absJärjend.append(abs(el))
    return absJärjend