def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for el in järjend:
        a = el.split()
        b = a[-1]
        if b == 'P':
            poisse += 1
        elif b == 'T':
            tüdrukuid += 1
    return (poisse, tüdrukuid)


            