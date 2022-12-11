def rek_abs(uus):
    uuslist=[]
    for el in uus:
        if isinstance(el, list):
            uuslist.append(rek_abs(el))
            
        else:
            uuslist.append(abs(el))
            
    return uuslist





