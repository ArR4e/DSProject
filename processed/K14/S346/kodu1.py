def rek_abs(maatriks):
    uus = []
    if maatriks == []:
        return []
    else:
        for i in maatriks:
            if isinstance(i, list):
               uus.append(rek_abs(i))
            else:
                uus.append(abs(i))
    return uus