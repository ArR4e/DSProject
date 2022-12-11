def rek_abs(n):
    jarjend = []
    
    for el in n:
        if isinstance(el, list):
            jarjend.append(rek_abs(el))
        else:
            jarjend.append(abs(el))
            
    return jarjend

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))