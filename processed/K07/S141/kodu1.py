def poisse_ja_tüdrukuid(nimi_ja_sugu):
    m = 0
    n = 0
    for i in nimi_ja_sugu:
        i.split()

        if i[-1] == "P":
            m += 1
        
        if i[-1] == "T":
            n += 1            
    return(abs(m), abs(n))

