def poisse_ja_tüdrukuid(list):
    poisse = 0
    tüdrukuid = 0
    for el in list:
        if el.endswith("P"):
            poisse = poisse + 1
        else:
            tüdrukuid = tüdrukuid + 1
    return poisse, tüdrukuid