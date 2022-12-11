def rek_abs(l):
    uuslist = []
    if not isinstance(l, list):
        return abs(l)
    if isinstance(l, list):
        for i in l:
            if isinstance(i, list):
                uuslist.append(rek_abs(i))
            else:
                uuslist.append(abs(i))
    return uuslist
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
        