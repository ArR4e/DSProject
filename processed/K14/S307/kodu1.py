def rek_abs(a):
    a1 = []
    for el in a:
        if isinstance(el, list):
            a1.append(rek_abs(el))
        else:
            a1.append(abs(el))
    return a1