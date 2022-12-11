def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    while True:
        for el in järjend:
            if el[-1] == "P":
                poisse += 1
            elif el[-1] == "T":
                tüdrukuid += 1
            else:
                break
        return (poisse, tüdrukuid)
