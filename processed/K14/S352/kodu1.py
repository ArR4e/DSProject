def rek_abs(arvud):
    jrj=[]
    if isinstance(arvud, list):
        for el in arvud:
            jrj.append(rek_abs(el))
    elif arvud<0:
        return -arvud
    else:
        return arvud
    return jrj