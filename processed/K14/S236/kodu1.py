#1. Rekursiivne absoluutväärtus

def rek_abs(järjend):
    abs_järjend = []
    for el in järjend:
        if isinstance(el, list):
            rek_abs(el)
        else:
            el = abs(el)
            abs_järjend.append(el)
        print(abs_järjend)
            

rek_abs(([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))