def rek_abs(jär):
    uus = []
    for i in range(len(jär)):
        if isinstance(jär[i], list) == True:
            uus.append(rek_abs(jär[i]))
        else:
            uus.append(abs(jär[i]))
    return uus