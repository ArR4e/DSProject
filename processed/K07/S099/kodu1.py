def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for isik in järjend:
        if isik[-1] == "P":
            poisse += 1
        elif isik[-1] == "T":
            tüdrukuid += 1
        else:
            print("Viga!")
    return (poisse, tüdrukuid)