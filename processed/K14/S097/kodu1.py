def rek_abs(järjend):
    uusjärjend = []
    for el in järjend:
        if isinstance(el, list) is False:
            if el < 0:
                el *= -1
                uusjärjend.append(el)
            else:
                uusjärjend.append(el)
        else:
            uusjärjend.append(rek_abs(el))
            
    return uusjärjend
