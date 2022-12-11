def seosta_lapsed_ja_vanemad(lapsedf,nimif):
    f=open(lapsedf,"r",encoding="UTF-8")
    g=open(nimif,"r",encoding="UTF-8")
    nimed={}
    lapsed={}
    for rida in g:
        rida=rida.rstrip()
        rida=rida.split(" ")
        nimed[rida[0]]=rida[1]+" "+rida[2]
    for rida in f:
        rida=rida.rstrip()
        rida=rida.split(" ")
        vanem=nimed[rida[0]]
        laps=nimed[rida[1]]
        if laps in lapsed:
            lapsed[laps].add(vanem)
        else:
            lapsed[laps]=set()
            lapsed[laps].add(vanem)
    return lapsed
    """for i in lapsed:
        if len(lapsed[i])==2:
            return(i+": "+str(lapsed[i][0])+", "+str(lapsed[i][1]))
        else:
            return(i+": "+str(lapsed[i][0]))"""
    f.close()
    g.close()

    