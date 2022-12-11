import copy

def rek_abs(järjend):
    tulemus = copy.deepcopy(järjend)
    if järjend == []:
        return tulemus
    for i in range(len(järjend)):
        if isinstance(järjend[i], list):
            tulemus[i] = rek_abs(järjend[i])
        else:
            tulemus[i] = abs(järjend[i])
    return tulemus

