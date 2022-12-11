def rek_abs(järjend):
    if järjend == []:
        return []
    else:
        uus_järjend = []
        for i in range(len(järjend)):
            if isinstance(järjend[i], list):
                uus_järjend.append(rek_abs(järjend[i]))
            else:
                if järjend[i] < 0:
                    uus_järjend.append(järjend[i] * -1)
                else:
                    uus_järjend.append(järjend[i])
    return uus_järjend
    
# print(rek_abs([1, -2, [-3, 4], -10]))