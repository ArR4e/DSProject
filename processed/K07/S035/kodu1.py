def poisse_ja_tüdrukuid(järjend):
    m=0
    n=0
    for nimi in järjend:
        b=0
        a=len(nimi)
        for char in nimi:
            b+=1
            if b==a and char=="P":
                m+=1
            if b==a and char=="T":
                n+=1
    ennik=(m, n)
    return ennik
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
    
            
            

    