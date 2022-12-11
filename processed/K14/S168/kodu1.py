from copy import deepcopy
    


def absolute(l):
    for i in range(len(l)):
        if not isinstance(l[i], list):
            l[i] = abs(l[i])
        else:
            absolute(l[i])
    return l

def rek_abs(l):
    a = deepcopy(l)
    return absolute(a)




print(rek_abs([17, [-18, [-19]]]))
