def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for nimi in järjend:
        nimi = nimi.split(" ")
        sugu = nimi[-1]
        if "P" in sugu:
            poisid += 1
        elif "T" in sugu:
            tüdrukud += 1
    return (poisid, tüdrukud)