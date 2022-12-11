def rek_abs(jarjend):
    jarUus = []
    for el in jarjend:
        if isinstance(el, list):
            jarUus.append(rek_abs(el))
        else:
            jarUus.append(abs(el))
    return jarUus

print(rek_abs([-1,-2,[2,-3],-4]))

    
    