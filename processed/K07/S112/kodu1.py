
def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    
    for sõne in järjend:
        
        sõne.split()
        
        if sõne[-1] == "P":
            poisid += 1
        elif sõne[-1] == "T":
            tüdrukud += 1
        else:
            continue
        
    return (poisid,tüdrukud)
