def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for rida in järjend:
        uus_järjend = rida.split(" ")
        uus_järjend2 = uus_järjend[-1]
        for rida in uus_järjend2:
            if rida == "P":
                poisid += 1
            if rida == "T":
                tüdrukud += 1
        
    return (poisid, tüdrukud)
        