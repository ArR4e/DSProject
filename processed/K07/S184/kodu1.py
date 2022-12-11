def poisse_ja_tüdrukuid(a):
    poisse=0
    tüdrukuid=0
    for i in a:
        a= i.split(" ")
        
        if "P" in a[-1]:
            poisse+=1
        elif "T" in a[-1]:
            tüdrukuid+=1
    b=(poisse, tüdrukuid)
    return b

poisse_ja_tüdrukuid(['Mati P', 'Tati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
