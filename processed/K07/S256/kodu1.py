def poisse_ja_tüdrukuid(list) -> bool:
    p_ja_T = ()
    poisid = 0
    tüdrukud = 0
    for el in list:
        if el.endswith("P"):
            poisid += 1
        elif el.endswith("T"):
            tüdrukud += 1
    return (poisid, tüdrukud)




