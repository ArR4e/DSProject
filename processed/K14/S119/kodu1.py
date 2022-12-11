def rek_abs(jarjend):
    new_jarjend = []
    for el in jarjend:
        if isinstance(el, list):
            new_jarjend.append(rek_abs(el))
        else:
            el = abs(el)
            new_jarjend.append(el)
    return new_jarjend

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))