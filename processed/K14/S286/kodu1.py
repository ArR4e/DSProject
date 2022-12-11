def rek_abs(x):
    vahepealne = []
    for el in x:
        if isinstance(el, list):
            vahepealne.append(rek_abs(el))
        else:
            vahepealne.append(abs(el))
    return vahepealne
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))