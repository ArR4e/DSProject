def rek_abs(järjend):
    järjend_abs = []
    for el in järjend:
        if isinstance(el, list) == 1:
            järjend_abs.append(rek_abs(el))
        else:
            järjend_abs.append(abs(el))
    return järjend_abs
#print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
#print(rek_abs([]))
