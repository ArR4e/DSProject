def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for i in range (len(järjend)):
        sugu = (järjend[i])[-1]
        if sugu == "P":
            poisid += 1
        else:
            tüdrukud += 1
    return((poisid, tüdrukud))