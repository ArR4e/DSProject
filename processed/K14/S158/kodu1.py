def rek_abs(m) :
    uus_list = []
    for i in m:
        if isinstance(i, list):
            uus_list.append(rek_abs(i))
        else:
            uus_list.append(abs(i))
    return uus_list

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))