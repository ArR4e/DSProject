def poisse_ja_tüdrukuid(people):
    poiste_arv = 0
    tudrukute_arv = 0
    for el in people:
        if el[-1] == 'P':
            poiste_arv += 1
        else:
            tudrukute_arv += 1
    return (poiste_arv, tudrukute_arv)
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))