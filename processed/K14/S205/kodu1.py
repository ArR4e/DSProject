def rek_abs(argument, järjend = None):
    if järjend == None:
        järjend = []
    for el in argument:
        if isinstance(el, list):
            järjend.append(rek_abs(el))
        else:
            järjend.append(abs(el))
    return järjend