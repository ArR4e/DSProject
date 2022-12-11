def rek_abs(arvud):
    tulemus=[]
    for el in arvud:
        if isinstance (el, float) or isinstance(el, int):
            tulemus.append(abs(el))
        if isinstance (el,list):
            tulemus.append(rek_abs(el))
    return tulemus
            

v=  rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]])
    