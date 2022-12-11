def rek_abs(jarjend):
    uus = []
    for i in jarjend:
        if isinstance(i, list):
            uus.append(rek_abs(i))
        else:
            uus.append(abs(i))
    return uus
        
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))