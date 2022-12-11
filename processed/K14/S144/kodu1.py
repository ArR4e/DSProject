def rek_abs(j):
    uus = []
    for i in j:
        if isinstance(i, list):
            uus.append(rek_abs(i))
        else:
            uus.append(abs(i))
    return uus