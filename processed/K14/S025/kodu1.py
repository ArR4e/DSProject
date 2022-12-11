def rek_abs(jär):
    uus = []
    for el in jär:
        if isinstance(el, list):
            uus.append(rek_abs(el))
        else:
            uus.append(abs(el))
    return uus