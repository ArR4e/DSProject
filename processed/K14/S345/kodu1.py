def rek_abs(järjend):
    uus = []
    if järjend == []:
        return []
    if isinstance(järjend[0], list):
        return rek_abs(järjend[0])
    else:
        if järjend[0] < 0:
            uus.append(järjend[0]*(-1))
            return rek_abs(järjend[1:])
        else:
            uus.append(järjend[0]
            return rek_abs(järjend[1:])
    

print(rek_abs([1, -2, 3]))