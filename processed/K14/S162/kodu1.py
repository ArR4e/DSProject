def rek_abs(järjend):
    uusjärjend=[]
    for el in järjend:
        if isinstance(el,list)==True:
            uusjärjend.append(rek_abs(el))
        else:
            uusjärjend.append(abs(el))
    return uusjärjend
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
