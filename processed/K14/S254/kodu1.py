# 1. Rekursiivne absoluutväärtus

def rek_abs(väärtus):
    if type(väärtus) != list:
        return abs(väärtus)
    elif väärtus == []:
        return väärtus
    else:
        sügavused = []
        for element in väärtus:
            elemendi_sügavus = rek_abs(element)
            sügavused.append(elemendi_sügavus)
        return sügavused    
            

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))