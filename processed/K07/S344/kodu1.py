poisid = 0
tüdrukud = 0

def poisse_ja_tüdrukuid(nimed):
    global poisid
    global tüdrukud
    for rida in nimed:
        uus_rida = rida.split(" ")
        if uus_rida[-1] == "P":
            poisid = poisid + 1
        if uus_rida[-1] == "T":
            tüdrukud = tüdrukud + 1
    return (poisid, tüdrukud)