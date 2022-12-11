def rek_abs(a):
    if isinstance(a, list):
        b = []
        for el in a:
            b.append(rek_abs(el))
        return b
    else:
        return abs(a)
