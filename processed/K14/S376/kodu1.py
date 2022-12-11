j = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]

def rek_abs(j):
    uus = []
    for el in j:
        if isinstance(el, list) == True:
            uus.append(rek_abs(el))
        else:
            uus.append(abs(el))
    return uus