#1. Rekursiivne absoluutväärtus

def rek_abs(järjend):
    uus_järjend=[]
    if järjend==[]:
        return järjend
    for element in järjend:
        if isinstance(element, list):
            uus_järjend.append(rek_abs(element))
        else:
            if element<0:
                element=-element
            uus_järjend.append(element)
    return uus_järjend

print(rek_abs([1, [2], -3]))
