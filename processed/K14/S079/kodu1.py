# 1. Rekursiivne absoluutväärtus
# Kirjuta rekursiivne funktsioon rek_abs, mis võtab argumentideks järjendi,
# mille elementideks võivad olla arvud ja/või järjendid. Igas alamjärjendis on jällegi arvud ja/või järjendid jne.
# Funktsioon peab tagastama uue sama kujuga andmestruktuuri, kus kõik arvud on asendatud nende absoluutväärtusega.
# Argumendiks antud järjendit ega ühtegi alamjärjendit muuta ei tohi.

# Näide funktsiooni kasutamisest:

# >>> rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]])
# [2, 6, [8, 12, 12, [4, [6], 3]], 7, [3.55, 3.55]]
# >>> rek_abs([])
# []
# VIHJE!

# >>> isinstance([1, 2, 3], list)
# True
# >>> isinstance(435, list)
# False

def rek_abs(järjend):
    if type(järjend) != list:
        return abs(järjend)
    else:
        if järjend == []:
            return []
        else:
            järjend1 = []
            for element in järjend:
                elemendid = rek_abs(element)
                järjend1.append(elemendid)
            return(järjend1)
                
# print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))    