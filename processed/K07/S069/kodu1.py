
def poisse_ja_tüdrukuid(jarjend):
    p = 0
    t = 0
    if len(jarjend) > 0:
        for element in jarjend:
            if element[-1] == 'P':
                p += 1
            else:
                t += 1
    ennik = (p, t)
    return ennik


print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))