def rek_abs(järjend):
    uus_järjend = []
    for indeks in range(len(järjend)):
        uus_järjend.append([])
        if isinstance(järjend[indeks], list):
            uus_järjend[indeks] = rek_abs(järjend[indeks])
        else:
            uus_järjend[indeks] = abs(järjend[indeks])
    return uus_järjend

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))