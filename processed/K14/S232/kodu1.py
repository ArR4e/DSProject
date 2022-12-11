def rek_abs(jarjend):
    uus_jarjend = []
    for i in range(len(jarjend)):
        if isinstance(jarjend[i], list) == True:
            uus_jarjend.append(rek_abs(jarjend[i]))
        else:
            uus_jarjend.append(abs(jarjend[i]))
    return uus_jarjend
            
rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]])