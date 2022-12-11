poiste_arv = 0
tüdrukute_arv = 0

def poisse_ja_tüdrukuid(järjend):
    global poiste_arv
    global tüdrukute_arv
    for i in järjend:
        uus_järjend = i.split(" ")
        if "P" in uus_järjend:
            poiste_arv+=1
        else:
            tüdrukute_arv+=1
    return (poiste_arv, tüdrukute_arv)


