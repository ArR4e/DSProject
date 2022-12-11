lst = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]

def rek_abs(lst):
    uuslist = []
    for i in lst:
        if isinstance(i, list):
            uuslist.append(rek_abs(i))
        else:
            uuslist.append(abs(i))        
    return uuslist

print(rek_abs(lst))