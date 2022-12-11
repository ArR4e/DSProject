def rek_abs(järg):
    for i in range(len(järg)):        
        if isinstance(järg[i], int) == True or isinstance(järg[i], float) == True:
            järg[i] = abs(järg[i])
        if isinstance(järg[i], list) == True:
            järg[i] = rek_abs(järg[i])
    return järg
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))