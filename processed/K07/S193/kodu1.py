def poisse_ja_tüdrukuid(järjend):
    tüdrukuid = 0
    poisse = 0

    for rida in järjend:
        m = rida[-1]
        if m == "T":
            tüdrukuid += 1
        if m == "P":
            poisse += 1
    return (poisse, tüdrukuid)
        





        