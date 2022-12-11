
def poisse_ja_tüdrukuid(nimed):
    poisse = 0
    tüdrukuid = 0
    
    for nimi in nimed:
        if nimi[-1] == "P":
            poisse += 1
        elif nimi[-1] == "T":
            tüdrukuid +=1
    return (poisse, tüdrukuid)

(poisse, tüdrukuid) = poisse_ja_tüdrukuid(["Mati P"])

print((poisse, tüdrukuid))


    