#alustasin 28.11.2021
def rek_abs(jarjend):
    if isinstance(jarjend, list) == False:
        return abs(jarjend)
    elif jarjend == []:
        return []
    else:
        jarjend1 = []
        for i in jarjend:
            jarjend1.append(rek_abs(i))
        return jarjend1