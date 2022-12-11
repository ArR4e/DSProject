def rek_abs(vana_järjend):
    järjend = vana_järjend[:]
    for indeks,element in enumerate(järjend):
        if isinstance(element,list) == True:
            järjend[indeks] = rek_abs(element)
        else:
            järjend[indeks] = abs(element)
    return järjend