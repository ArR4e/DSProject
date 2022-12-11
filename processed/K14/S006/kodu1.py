def rek_abs(järjend):
    uus = []
    if järjend == []:
        return uus
    else:
        for element in järjend:
            if not isinstance(element, list):
                uus.append(abs(element))
            else:
                uus.append(rek_abs(element))
    return uus

#print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))