def rek_abs(lst):
    uuslst = []
    if type(lst) == list:
        for i in lst:
            uuslst.append(rek_abs(i))
    else:
        if lst < 0:
            return -lst
        else:
            return lst
    return uuslst