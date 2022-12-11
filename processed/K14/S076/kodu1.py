def rek_abs(järjend):
    vastus = []
    for i in järjend:            
        if isinstance(i, list):
            vastus.append(rek_abs(i))
        else:
            vastus.append(abs(i))
    return vastus