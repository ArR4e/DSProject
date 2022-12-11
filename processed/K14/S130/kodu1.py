

def rek_abs(jarjend):
    uusjarjend = []
    for element in jarjend:
        if isinstance(element, list):
            uusjarjend.append(rek_abs(element))
        else:
            uusjarjend.append(abs(element))
    return uusjarjend