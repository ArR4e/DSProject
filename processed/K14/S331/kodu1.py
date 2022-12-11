def rek_abs(järjend):
    järjend1 = []
    for el in järjend:
        if isinstance(el, list):
            järjend1.append(rek_abs(el))
        else:
            uus_el = abs(el)
            järjend1.append(uus_el)
    return järjend1