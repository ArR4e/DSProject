def rek_abs(järjend):
    uusjarj = järjend[:]
    for i in uusjarj:
        if isinstance(i, list):
             uusjarj[järjend.index(i)] = rek_abs(i)
        else:
            uusjarj[järjend.index(i)] = abs(i)
    return uusjarj


