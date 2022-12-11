def rek_abs(jarjend):
    if type(jarjend) != list:
        return abs(jarjend)
    else:
        uus_jarjend = []
        for el in jarjend:
            uus_jarjend.append(rek_abs(el))
        return uus_jarjend
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))