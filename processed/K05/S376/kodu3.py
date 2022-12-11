def moos(suured_karbid, väiksed_karbid, kg):

    karbid_kasutusel = 0
    karbid_otsas = ""
    
    while kg >= 5 and suured_karbid > 0:
        kg -= 5
        karbid_kasutusel += 1
        suured_karbid -= 1
        
    while kg > 0 and väiksed_karbid > 0:
        kg -= 1
        karbid_kasutusel += 1
        väiksed_karbid -= 1
    
    if suured_karbid == 0 or väiksed_karbid == 0:
        karbid_otsas = True
        
    if kg > 0 and karbid_otsas == True:
        return -1

    return karbid_kasutusel