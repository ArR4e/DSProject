def rek_abs(järjend):
    j = []
    for i in järjend:
        if isinstance(i, list):
            j.append(rek_abs(i))
        else:
            if i < 0:
                j.append(-i)
            else:
                j.append(i)
    return(j)
        
        