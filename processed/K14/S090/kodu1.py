def rek_abs(n):
    for i in n:
        if isinstance(i, list) == True:
            rek_abs(i)
        else:
            indeks = n.index(i)
            n[indeks] = abs(i)
    return n