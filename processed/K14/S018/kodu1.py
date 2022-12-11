def rek_abs(jär,mag=[]):
    for i in jär:
        if isinstance(i, list) == True:
            mag.append(rek_abs(i,[]))
        else:
            mag.append(abs(i))
    return mag