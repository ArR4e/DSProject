def poisse_ja_tüdrukuid(nimi_sugu):
    poisid = []
    tüdrukud = []
    
    for i in nimi_sugu:
        osa = i.split()
        nimi = osa[0]
        sugu = osa[-1]
        
        if sugu == "P":
            poisid += [nimi]
        else:
            tüdrukud += [nimi]
        
    m = len(poisid)
    n = len(tüdrukud)
    return (m,n)






print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
