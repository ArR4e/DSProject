def rek_abs(j):
    n = []
    if isinstance(j, list):
        for i in range(len(j)):
            n.append(rek_abs(j[i]))
        return n
    else:
        return abs(j)
    
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))