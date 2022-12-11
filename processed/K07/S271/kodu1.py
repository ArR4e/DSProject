def poisse_ja_tüdrukuid(jarjend):
    poisse = 0
    tudrukuid = 0
    for rida in jarjend:
        if rida[-1:] == 'P':
            poisse += 1
        elif rida[-1:] == 'T':
            tudrukuid += 1
    ennik = (poisse, tudrukuid)
    return ennik