def rek_abs(järjend):
    järjend_abs = []
    for element in järjend:
        if isinstance(element, list) == 1:
            järjend_abs.append(rek_abs(element))
        else:
            järjend_abs.append(abs(element))
    return järjend_abs

print(rek_abs([2, -6, [8, -12, -12, [4, [-10], -3]], 7, [3.55, -3.55]]))