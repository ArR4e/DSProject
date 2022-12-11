def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for rida in järjend:
        uus_järjend = rida.split(" ")
        if uus_järjend[-1] == "P":
            poisid += 1
        elif uus_järjend[-1] == "T":
            tüdrukud += 1
    return (poisid, tüdrukud)
            
        