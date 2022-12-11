def rek_abs(järjend):
    abs_järjend = []
    for element in järjend:
        if isinstance(element, list) == True:
            abs_järjend.append(rek_abs(element))
        else:
            abs_element = abs(element)
            abs_järjend.append(abs_element)
    return abs_järjend