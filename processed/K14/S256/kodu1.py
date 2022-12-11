def rek_abs(järjend, uuslist = []):
    for el in järjend:
        if isinstance(el, list):
            lisatav = rek_abs(el, uuslist = [])
            uuslist.append(lisatav)
        else:
            uuslist.append(abs(el))
                
    return uuslist
        
        
        
        
print(rek_abs([-4,5,[3,-4],6,7,-5.4,[[4,-27,6],-0.56],-8]))