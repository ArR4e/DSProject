def rek_abs(järjend):
    uus_järjend = []
    if len(järjend) == 0:
        return []
    else:
        for element in järjend:
            if isinstance(element, list):
                rek_abs(element)
            else:
                uus_järjend += [(abs(element))]
                return uus_järjend
            
rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]])