def rek_abs(sisend):
    if isinstance(sisend, list):
        for i in range(len(sisend)):
            sisend[i] = rek_abs(sisend[i])
        return sisend
    else:
        return abs(sisend)
