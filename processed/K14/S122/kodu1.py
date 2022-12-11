def rek_abs(järjend):
    if järjend == []:
        return []
    else:
        uus_järjend = []
        for el in järjend:
            if isinstance(el,list):
                uus_järjend.append(rek_abs(el))
            else:
                uus_järjend.append(abs(el))
    return uus_järjend

järjend=[]
print(rek_abs(järjend))