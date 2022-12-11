def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for element in järjend:
        laps = element.split()
        sugu = laps[-1]
        if sugu == 'P':
            poisse += 1
        else:
            tüdrukuid += 1
    return (poisse, tüdrukuid)

