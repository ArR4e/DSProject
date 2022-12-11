def rek_abs(n):
    tühi = []
    for el in n:
        while isinstance(el, list):
            rek_abs(el)
            tühi.append(el)
        else:
            tühi.append(abs(el))
    return(tühi)

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))