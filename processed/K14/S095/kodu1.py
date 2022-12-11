def rek_abs(x):
    abs_list=[]
    for el in x:
        if isinstance(el, list):
            abs_list.append(rek_abs(el))
        else:
            abs_list.append(abs(el))
    return abs_list