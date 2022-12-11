def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for el in (järjend):
        sugu = el.split(" ")[-1]
        if sugu == "P":
                poisid += 1
        elif sugu == "T":
                tüdrukud += 1
    return (poisid, tüdrukud)

        
    