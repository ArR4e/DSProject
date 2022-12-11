def rek_abs(jär):
    j = []
    for el in jär:
        if not isinstance(el, list):
            j.append(abs(el))
        else:
            j.append(rek_abs(el))
    return j