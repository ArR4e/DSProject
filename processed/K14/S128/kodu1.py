#Rekursiivne absoluutväärtus
def rek_abs(järjend):
    uus_järjend = []
    if järjend == []:
        return []
    else:
        for i in range(len(järjend)):
            if isinstance(järjend[i], list) == False:
                uus_järjend.append(abs(järjend[i]))
            else:
                uus_järjend.append(rek_abs(järjend[i]))
        return uus_järjend

