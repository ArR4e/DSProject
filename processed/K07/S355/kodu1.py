def poisse_ja_tüdrukuid(minulist):
    
    tarv = 0
    parv = 0
    for nimi in minulist:
        nimi = nimi[::-1]
        if nimi[0] == "T":
            tarv +=1
        else:
            parv +=1
            
    return (parv, tarv)
            
    
    
minulist = ["Theresa T", "Madis P", "Rasmus P", "Rain P", "Hanna T", "Robin P", "Alvar P"]
poisse_ja_tüdrukuid(minulist)
