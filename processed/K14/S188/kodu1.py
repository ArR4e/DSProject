def rek_abs(jarjend):
    jarjend = jarjend[:]
    if jarjend == []:
        return jarjend
    pea = jarjend[0]
    saba = jarjend[1:]
    if not isinstance(pea, list):
        pea = abs(pea)
    else:
        pea = rek_abs(pea)
    return [pea] + rek_abs(jarjend[1:])