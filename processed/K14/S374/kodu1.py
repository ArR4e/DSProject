def rek_abs(massiiv):
    jarjend = massiiv.copy()
    
    for i in range(len(jarjend)):
        if isinstance(jarjend[i], list) == True:
            jarjend[i] = rek_abs(jarjend[i])
        else:
            jarjend[i] = abs(jarjend[i])
                
    return jarjend
        