def rek_abs(järjend):
    tulemus = []
    for el in järjend:
            if isinstance(el, list):
                tulemus.append(rek_abs(el))
            else:
                tulemus.append(abs(el))
    return tulemus
print(rek_abs([-1,-4,-6,[1,-3]]))