def rek_abs(m):
    for rida in range(len(m)):
        if isinstance(m[rida],list)==True:
            rek_abs(m[rida])
        else:
            m[rida]=abs(m[rida])
    return m
print(rek_abs([[2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]]))

