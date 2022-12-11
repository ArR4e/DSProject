def poisse_ja_tüdrukuid(x):
    poisid = 0
    tüdrukud = 0

    for el in x:
        eraldi = el.split(" ")
        
        for el in eraldi:
            if el == "P":
                poisid += 1
            elif el == "T":
                tüdrukud += 1
            else:
                continue

    return (poisid, tüdrukud)