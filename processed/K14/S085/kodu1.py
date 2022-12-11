def rek_abs(järjend):
    jrj = []
    if len(järjend) == 0:
        return []
    else:
        for el in järjend:
            if isinstance(el, list):
                jrj.append(rek_abs(el))
            else:
                jrj.append(abs(el))
        return jrj
