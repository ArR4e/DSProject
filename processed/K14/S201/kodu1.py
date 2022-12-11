def rek_abs(a):
    uus_list=[]
    for el in a:
        if isinstance(el, list):
            uus_list.append(rek_abs(el))
        else:
            uus_list.append(abs(el))
    return uus_list