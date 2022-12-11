def rek_abs(li):
    for i, el in enumerate(li):
        if isinstance(el, list) == False:
            li[i] = abs(el)
        else:
            li[i] = rek_abs(el)
    return li

jarjend = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]

print(rek_abs(jarjend))
            