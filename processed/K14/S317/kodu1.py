def rek_abs(järjend):
    uusjärjend = []
    for i in järjend:
        if isinstance(i, list) == True:
            uusjärjend.append(rek_abs(i))
        else:
            uusjärjend.append(abs(i))
    return uusjärjend
rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]])