def rek_abs(järjend):
    väljund = []
    for el in järjend:
        if isinstance(el, list):
            väljund.append(rek_abs(el))
        
        else:
            väljund.append(abs(el))        
        
    return väljund