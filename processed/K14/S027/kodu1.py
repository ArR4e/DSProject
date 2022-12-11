def rek_abs(x):
    abs_jär = []
    for el in x:
        if isinstance(el, list):
            abs_jär.append(rek_abs(el))
        else:
            abs_jär.append(abs(el))
    return abs_jär
        
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))