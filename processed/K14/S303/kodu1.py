def rek_abs(jarjend):
    uus_jarjend = []
    for i in jarjend:
        if isinstance(i, list):
            uus_jarjend.append(rek_abs(i))
        else:
            uus_jarjend.append(abs(i))
        
    return uus_jarjend
