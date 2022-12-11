def rek_abs(järjend):
    uusjärjend = []
    if järjend == []:
        return uusjärjend
    else:
        for el in järjend:
            if isinstance(el, list) is False:
                uusjärjend.append(abs(el))
            else:
                uusjärjend.append(rek_abs(el))
        return uusjärjend

