from copy import *
#j = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
def rek_abs(j):
    uus_j = []
    for el in j:
        if isinstance(el, list) == False:
            uus_j += [abs(el)]
        if isinstance(el, list) == True:
            uus_j += [rek_abs(el)]
    return uus_j
    
    
    
#print(rek_abs(j))