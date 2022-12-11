def rek_abs(j1):
    if j1 == []:
        return j1
    if not isinstance(j1, list):
        return abs(j1)
    else:
        j2 = [rek_abs(j1[0])]
        j2 += rek_abs(j1[1:])
        return j2