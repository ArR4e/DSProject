def rek_abs(järjend):
    
    if len(järjend) == 0:
        return []
    
    uus = []
    for el in järjend:
        if isinstance(el, list):
            uus.append(rek_abs(el))
            
        else:
            uus.append(abs(el))
            rek_abs(järjend[1:])
    
    return uus
                

        
    