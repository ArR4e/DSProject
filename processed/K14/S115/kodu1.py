def rek_abs(väärtus):
    if isinstance(väärtus, list) == False:
        return abs(väärtus) 
    elif väärtus == []:
        return []
    elif isinstance(väärtus, list) == True:
        uus = []
        for el in väärtus:
            sügavus = rek_abs(el)
            uus.append(sügavus)
    return uus

print(rek_abs([2, -6, [8, -12,-12, [4, [-6], -3]], 7, [3.55, -3.55]]))