# Oli abiks:
# https://stackoverflow.com/questions/47807738/absolute-value-from-nested-list-using-recursion

def rek_abs(j):
    uus_j = []
    if j == []:
        return []
    if isinstance(j, list):
        # kui on list.
        for el in j:
            uus_j.append(rek_abs(el))            
        return uus_j
    else:
        # pole list.
        return abs(j)
