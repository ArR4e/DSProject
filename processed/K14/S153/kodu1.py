def rek_abs(lst):
    uus = []
    if lst == []:
        return []
    else:
        for el in lst:
            if type(el) == int or type(el) == float:
                uus.append(abs(el))
            else:
                uus.append(rek_abs(el))
        return uus