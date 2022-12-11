def rek_abs(järjend):
    u=[]
    for el in järjend:
        if isinstance(el, list):
            u.append(rek_abs(el))
        else:
            u.append(abs(el))
            
    return u
rek_abs([])