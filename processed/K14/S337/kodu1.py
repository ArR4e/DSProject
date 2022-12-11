def rek_abs(jär):
    vastus = []
    for el in jär:
        if isinstance(el, list):
            vastus.append(rek_abs(el))
        else:
            vastus.append(abs(el))
    return vastus