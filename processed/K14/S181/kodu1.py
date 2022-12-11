def rek_abs(järjend):
    järjend2 = []
    for i in järjend: järjend2.append(rek_abs(i)) if isinstance(i,list) else järjend2.append(abs(i))
    return järjend2