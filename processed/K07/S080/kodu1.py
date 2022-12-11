def poisse_ja_tüdrukuid(järjend):
    null = 0
    a = 0
    poiss = 0
    tüdrukuid = 0
    for poisse in järjend:
        if järjend[a][-1:] == 'P':
            poiss = poiss +1
            a = a + 1
        elif järjend[a][-1:] == 'T':
            tüdrukuid = tüdrukuid + 1
            a = a+1
        elif järjend[a][-1:] == '':
            null = null
            a = a + 1
    if poiss != 0 and tüdrukuid != 0:
        return(poiss,tüdrukuid)
    elif poiss == 0 and tüdrukuid != 0:
        return(null,tüdrukuid)
    elif poiss != 0 and tüdrukuid == 0:
        return(poiss,null)
    else:
        return(null,null)
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
poisse_ja_tüdrukuid([])
poisse_ja_tüdrukuid(['Mati P','Siim Aleksander P','Jüri P'])
        
            
    