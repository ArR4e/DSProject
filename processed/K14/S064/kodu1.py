# 1. Rekursiivne absoluutväärtus

def rek_abs(järjend):
    uus_järjend = []
    for el in järjend:
        if isinstance(el, list):
            uus_järjend.append(rek_abs(el))
        else:
            uus_järjend.append(abs(el))
    return uus_järjend
            
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))

#isinstance([1, 2, 3], list)
#True
#isinstance(435, list)
#False
#print(rek_abs([]))