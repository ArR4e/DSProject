def rek_abs(l):
    uus = []
    for el in l:
        if isinstance(el , list) is True:
            uus.append(rek_abs(el))
        elif isinstance(el, list) is False:
            uus.append(abs(el))
            
    return uus

c = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
print(rek_abs(c))