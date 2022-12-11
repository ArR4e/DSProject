def rek_abs(järjend):
    abs_järjend = []
    
    for el in järjend:
        if isinstance(el, list):
            abs_järjend.append(rek_abs(el))
        
        else:
            abs_järjend.append(abs(el))
            
    return abs_järjend