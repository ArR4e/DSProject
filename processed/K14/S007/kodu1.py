def rek_abs(järjend):
    uus_järjend = []
    for el in järjend:
        if isinstance(el, list):
            uus_järjend.append(rek_abs(el))
        else:
            uus_järjend.append(abs(el))
    return uus_järjend

        
        
        

print(rek_abs([]))