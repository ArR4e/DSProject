def rek_abs(a):
    uuslist = []
    for e in a:
        if isinstance(e, list):
            uuslist.append(rek_abs(e))
        else:
            if e < 0:
                uuslist.append(e*-1)
            else:
                uuslist.append(e)
    return uuslist
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
print(rek_abs([]))