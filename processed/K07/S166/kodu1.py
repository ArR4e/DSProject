#poisse_ja_tüdrukuid(["blabla P","blabla T","blabla P"])
def poisse_ja_tüdrukuid(järjend):
    poisid=0
    tüdrukud=0
    for i in range(len(järjend)):
        nimi=järjend[i]
        sugu= nimi[-1]
        if sugu == "P":
            poisid+=1
        elif sugu == "T":
            tüdrukud+=1
    arv = (poisid,tüdrukud)
    return arv
