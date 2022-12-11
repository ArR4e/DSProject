def poisse_ja_tüdrukuid(järjend):
    m=0
    n=0
    for i in järjend:
        if i.endswith("T"):
            n+=1
        elif i.endswith("P"):
            m+=1
    return (m,n)
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])