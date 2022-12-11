def rek_abs(jar):
    uus_jar = []
    for el in jar:
        if isinstance(el, list):
            uus_jar.append(rek_abs(el))
        else:
            el = abs(el)
            uus_jar.append(el)
    return uus_jar
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))