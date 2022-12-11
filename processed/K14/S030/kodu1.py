def rek_abs(järjend):
    uus_järjend = []
    for element in järjend:
        if isinstance(element, list):
            uus_järjend.append(rek_abs(element))
        else:
            uus_järjend.append(abs(element))
    return uus_järjend

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))