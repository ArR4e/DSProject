def rek_abs(järjend):
    vastus = []
    for el in järjend:
        if isinstance(el, list):
            vastus.append(rek_abs(el))    
        else:
            vastus.append(abs(el))
    return vastus