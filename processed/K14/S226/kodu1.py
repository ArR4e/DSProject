l = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
def rek_abs(jarjend):
    ul = []
    for el in jarjend:
        if isinstance(el, list):
            ul.append(rek_abs(el))
        else:
             el = abs(el)
             ul.append(el)
    return ul

print(rek_abs(l))