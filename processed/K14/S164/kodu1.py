def rek_abs(järjend):
    uus_järjend = []
    if len(järjend) == 0 :
        return uus_järjend
    else:
        for element in järjend:
            if isinstance(element, list):
                uus_järjend.append(rek_abs(element))
            else:    
                abs_väärtus = abs(element)
                uus_järjend.append(abs_väärtus)
    
    return uus_järjend