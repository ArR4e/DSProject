def poisse_ja_tüdrukuid(järjend):
    try:
        m=0
        n=0
        for i in järjend:
            if i[-1] == "P":
                m+=1
            elif i[-1] == "T":
                n+=1
        ennik=(m,n)
        return ennik
    except:
        return (0,0)