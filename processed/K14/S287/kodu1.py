def rek_abs(järjend):
    abs_järjend = []
    
    if type(järjend) == int or type(järjend) == float:
        return abs(järjend)
    
    for i in järjend:
        if type(i) == list:
            abs_järjend.append(rek_abs(i))
        else:
            abs_järjend.append(abs(i))
            
    return abs_järjend
