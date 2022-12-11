def rek_abs(järjend):
    uus=[]
    for element in järjend:
        if isinstance(element, list):
            uus.append(rek_abs(element))
        else:
            uus += [abs(element)]
    return uus
# ei oska säilitada järjendeid järjendi sees