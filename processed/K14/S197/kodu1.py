def rek_abs(a):
    b = []
    for i in a:
        if isinstance(i, list):
            b.append(rek_abs(i))
        else:
            b.append(abs(i))
    return b