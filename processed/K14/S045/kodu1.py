def rek_abs(järjend):
    new_list = list()
    for item in järjend:
        if isinstance(item, list): new_list.append(rek_abs(item))
        else: new_list.append(abs(item))
    return new_list