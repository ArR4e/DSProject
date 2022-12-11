def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for nimi in järjend:
        if "P" == nimi[-1]:
            poisse += 1
        elif "T" == nimi[-1]:
            tüdrukuid += 1
    return poisse, tüdrukuid
