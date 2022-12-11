jär=[2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
def rek_abs(j):
    for indeks in range(len(j)):
        if isinstance(j[indeks], list):
            rek_abs(j[indeks])
        elif j[indeks]==[]:
            return []
        else:
            j[indeks]=abs(j[indeks])
    return j
print(rek_abs(jär)) # Ei jõudnud kahjuks töötava lahenduseni.