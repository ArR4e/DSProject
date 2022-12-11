def poisse_ja_tüdrukuid(järjend):
    poisid=0
    tüdrukud=0
    for el in järjend:
        el.split()
        if el[-1]=="P":
            poisid+=1
        if el[-1]=="T":
            tüdrukud+=1    
    return (poisid,tüdrukud) 