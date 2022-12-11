def poisse_ja_tüdrukuid(järjend):
    uus_järjend= []
    for rida in järjend:
        täht = rida[-1]
        uus_järjend.append(täht)
    poisse = uus_järjend.count("P")
    tüdrukuid = uus_järjend.count("T")
    return(poisse, tüdrukuid)
       