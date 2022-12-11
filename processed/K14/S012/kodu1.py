#nädal 14, kodu1

def rek_abs(järjend):
    uus_järjend = []
    for element in järjend:
        if isinstance(element, list):
            uus_järjend.append(rek_abs(element))
        else:
            uus_järjend.append(abs(element))
    return uus_järjend
            

