def rek_abs(järjend):
    for element in järjend:
        if isinstance(element, list):
            rek_abs(element)
        else:
            järjend[järjend.index(element)] = abs(element)
    return järjend
