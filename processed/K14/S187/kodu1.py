def rek_abs(jar):
    uus = []
    for asi in jar:
        if isinstance(asi, list):
            uus.append(rek_abs(asi))
        elif type(asi) == float:
            uus.append((asi**2)**0.5)
        else:
            uus.append(int((asi**2)**0.5))
    return uus