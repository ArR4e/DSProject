def rek_abs(jar):
    for el in jar:
        if type(el) == list:
            rek_abs(el)
        else:
            jar[jar.index(el)] = abs(el)
    return jar