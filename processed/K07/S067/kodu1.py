def  poisse_ja_tüdrukuid(nimed):
    poisid = 0
    tüdrukud = 0
    for i in nimed:
        if ' P' in i:
            poisid += 1
        if ' T' in i:
            tüdrukud += 1
        else:
            continue
    return (poisid, tüdrukud)
print(poisse_ja_tüdrukuid([]))
            