def rek_abs(järjend):
    uusjärjend = []
    for el in järjend:
        if isinstance(el,list):
            uusjärjend.append(rek_abs(el))
        else:
            if el < 0:
                uusjärjend.append(-el)
            else:
                uusjärjend.append(el)            
       
    return uusjärjend

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))