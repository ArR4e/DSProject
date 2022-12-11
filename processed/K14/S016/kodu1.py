def rek_abs(järjend):
    x = []
    for el in järjend:
        if isinstance(el, list):
            y = rek_abs(el)
            x.append(y)
        else:
            x.append(abs(el))
    return x
            
print(rek_abs([-2, 6, [-3]]))