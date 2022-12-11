def rek_abs(järjend):
    abilist = []
    for arv in järjend:
        if isinstance(arv, list):
            abilist.append(rek_abs(arv))
        else:
            abilist.append(abs(arv))
    return abilist

        
        
#print(rek_abs([3, -11, 0, 4, [0, -12], ]))