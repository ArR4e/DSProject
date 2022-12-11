def rek_abs(järjend, tase = 0, tulemus = []):
    for i in järjend:
        if type(i) == int:
            tulemus.append(i)
        elif type(i) == list:
            rek_abs(i, tase + 1, tulemus)
    return tulemus
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))