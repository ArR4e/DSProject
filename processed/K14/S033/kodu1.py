a = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]

def rek_abs(jär):
    uus = []
    for el in jär:
        if isinstance(el, list):
            uus.append(rek_abs(el))

        else:
            uus.append(abs(el))

    return uus

print(rek_abs(a))
    
