def rek_abs(järj):
    uus_järj = []
    for el in järj:
        if isinstance(el,list) == True:
            uus_järj += [rek_abs(el)]
        else:
            uus_järj += [abs(el)]
            
    return uus_järj