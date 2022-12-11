def poisse_ja_tüdrukuid(järjend):
    if järjend==[]:
        return (0,0)
    poisid=0
    tüdrukud=0
    for el in järjend:
        sugu=el[::-1]
        if sugu[0]=="P":
            poisid+=1
        elif sugu[0]=="T":
            tüdrukud+=1
    return (poisid, tüdrukud)
             
järjend=[]
print(poisse_ja_tüdrukuid(järjend))
