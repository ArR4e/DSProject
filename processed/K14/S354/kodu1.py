def rek_abs(a):
    if type(a) != list:
        a = abs(a)
        return a
    if a == []:
        return []
    else:
        for el in range(len(a)):
            a[el] = rek_abs(a[el])
        return a