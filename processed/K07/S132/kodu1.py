def poisse_ja_tüdrukuid(jarjend):
    poisse = 0
    tudrukuid = 0
    for inimene in jarjend:
        jupid = inimene.split()
        if jupid[-1] == 'P':
            poisse += 1
        else:
            tudrukuid += 1
    return poisse, tudrukuid