def rek_abs(a):
    uus_jär = []
    if isinstance(a, list):
        for el in a:
            uus_jär.append(rek_abs(el))
        return uus_jär
    else:
        return (abs(a))
