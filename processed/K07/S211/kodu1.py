def poisse_ja_tüdrukuid(järjend):
    
    if len(järjend)==0:
        return(0, 0)
    else:
        poisid = 0
        tüdrukud = 0
        for el in järjend:
            jupid = el.split(" ")
            pikkus = len(jupid)
            sugu = jupid[-1]
            
            if sugu == "P":
                poisid += 1
            elif sugu == "T":
                tüdrukud += 1
        
    return(poisid, tüdrukud)