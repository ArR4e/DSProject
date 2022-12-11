def rek_abs(järjend):
    absoluut = []
    for element in järjend:
        if isinstance(element, list):
            absoluut.append(rek_abs(element))
        else:
            absoluut.append(abs(element))
    return absoluut