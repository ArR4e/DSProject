def rek_abs(jarjend):
    uus_jarjend = []
    for element in jarjend:
        if isinstance(element, list):
            rek_abs(element)
        else:
            if element >= 0:
                element = element
                uus_jarjend = uus_jarjend + [element]
            else:
                element = -element
                uus_jarjend = uus_jarjend + [element]
    print(uus_jarjend)
rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]])