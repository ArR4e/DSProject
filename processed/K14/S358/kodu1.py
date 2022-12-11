#reb_abs

def rek_abs(target):
    rval = []
    for el in target:
        if isinstance(el, list) == True:
            rval.append(rek_abs(el))
        else:
            rval.append(abs(el))
    return rval

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))