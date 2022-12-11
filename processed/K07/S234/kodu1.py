def poisse_ja_tüdrukuid (nimekiri):
    poisse=0
    tüdrukuid=0
    for a in range(len(nimekiri)):
        nimekiri[a]=nimekiri[a].split()
        if nimekiri[a][len(nimekiri[a])-1]=="P":
            poisse+=1
        else:
            tüdrukuid+=1
    return(poisse,tüdrukuid)