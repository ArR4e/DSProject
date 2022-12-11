def rek_abs(jarjend):
    uus_jarjend = []
    for element in jarjend:
        if isinstance(element, list):
            uus_jarjend += [rek_abs(element)]
        else:
            if element < 0:
                uus_jarjend += [element * (-1)]
            else:
                uus_jarjend += [element]
    return uus_jarjend
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))