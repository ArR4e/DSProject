def rek_abs(järjend):
    abso = []
    for el in järjend:
        if isinstance(el, list):
            abso.append(rek_abs(el))
        else:
            abso.append(abs(el))
    
    return abso

print(rek_abs([2,-6,23,2,-55,2]))