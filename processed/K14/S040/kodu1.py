def rek_abs(x):
    uus_x = []
    for i in x:
        if isinstance(i, list):
            uus_x.append(rek_abs(i))
        else:
            uus_x.append(abs(i))
    return uus_x