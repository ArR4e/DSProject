def rek_abs(a):
    järjend = []
    for el in a:
        if isinstance(el, list):
            järjend.append(rek_abs(el))
        else:
            järjend.append(abs(el))
    return järjend
        