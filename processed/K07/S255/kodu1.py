def poisse_ja_tüdrukuid(list):
    poisid = 0
    tudrukud = 0
    for i in list:
        if i.endswith(" P"):
            poisid += 1
        else:
            tudrukud += 1
    return (poisid, tudrukud)