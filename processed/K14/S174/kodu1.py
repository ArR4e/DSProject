def rek_abs(jär):
    jär_abs = []
    for el in jär:
        if isinstance(el, list) == 1:
            jär_abs.append(rek_abs(el))
        else:
            jär_abs.append(abs(el))
            
    return jär_abs

#print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
#print(rek_abs([]))