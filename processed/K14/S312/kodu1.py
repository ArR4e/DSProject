import copy

def rek_abs(sisend):
    järjend = copy.deepcopy(sisend)
    for i in järjend:
        if isinstance(i, list):
             koht = järjend.index(i)
             uus = rek_abs(i)
             järjend[koht] = uus
        else:
            koht = järjend.index(i)
            järjend[koht] = abs(i)
    return järjend        
        
