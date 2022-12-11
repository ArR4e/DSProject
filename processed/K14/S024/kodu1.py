def rek_abs(jär):
    uus_jär = []
    for el in jär:
        if isinstance(el, list) == True:
            uus_jär.append(rek_abs(el))
        else:
            uus_jär.append(abs(el))
    return uus_jär
            
    