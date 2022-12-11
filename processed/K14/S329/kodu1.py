# 1. Rekursiivne absoluutväärtus

def rek_abs(järjend):
    uus_järjend = []
    if järjend == []:
        return uus_järjend
    for el in range(len(järjend)):
        try:
            if järjend[el] < 0:
                uus_järjend.append(-(järjend[el]))
            else:
                uus_järjend.append(järjend[el])
        except:
            uus_järjend.append(rek_abs(järjend[el]))
    return uus_järjend   
    
#print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
#print(rek_abs([1, -3, 20, [-10, -5], []]))