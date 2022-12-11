def rek_abs(a):
    uus = []
    for elem in a:
        if isinstance(elem, list):
            uus.append(rek_abs(elem))
        else:
            uus.append(abs(elem))
    return uus