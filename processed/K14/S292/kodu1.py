jada = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]


def rek_abs(jada):
    if isinstance(jada, list) == False:
        return abs(jada)
    else:
        tyhi = []
        for i in range(len(jada)):
            tyhi.append(rek_abs(jada[i]))
        return tyhi
            
            
            
print(rek_abs(jada))