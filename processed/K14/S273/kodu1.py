def rek_abs(järjend):
    for n in järjend:
        if isinstance(n, list) == False:
            järjend[järjend.index(n)] = abs(n)
        if isinstance(n, list) == True:
            rek_abs(järjend[järjend.index(n)])
    return järjend

# print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))