def rek_abs(järjend):
    väärtused = []
    for el in järjend:
        if isinstance(el,list) == False:
            väärtused.append(abs(el))
        else:
            väärtused.append(rek_abs(el))
    return väärtused
