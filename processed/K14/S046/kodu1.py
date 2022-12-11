def rek_abs(j):
    j1 = []
    if type(j)==list:
        for el in j:
            j1.append(rek_abs(el))
        return j1
    else:
        return(abs(j))
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))