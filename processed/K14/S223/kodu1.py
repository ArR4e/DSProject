def rek_abs(var):
    if type(var) != list:
        return abs(var)
    else:
        array = []
        for x in var:
            array += [rek_abs(x)]
        return array       
    
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))