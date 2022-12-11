def rek_abs(jär):
    uus_jär = []
    for el in jär:
        if isinstance(el, list):
            uus_jär.append(rek_abs(el))
        else:
            uus_jär.append(abs(el))
    return uus_jär

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))


