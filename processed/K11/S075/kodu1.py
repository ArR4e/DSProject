def seosta_lapsed_ja_vanemad(f1,f2):
    num=0
    g1=open(f1)
    kokku=""
    üks=""
    teine=""
    for rida in g1:
        vanemakood=rida.strip().split()[0]
        lapsekood=rida.strip().split()[1]
        g2=open(f2)
        for rida2 in g2:
            if rida2.strip().split()[0]==lapsekood:
                lapsenimi=" ".join(rida2.strip().split()[1:])
                laps=lapsenimi
            elif rida2.strip().split()[0]==vanemakood:
                vanemanimi=" ".join(rida2.strip().split()[1:])
                üks=vanemanimi
        if laps in kokku:
            järjend=kokku.split("\n")
            for i in järjend:
                num+=1
                vajalik=i.split(":")
                if vajalik[0]==laps:
                    mõlemad=üks+","+vajalik[1]
                    vajalik[num]=mõlemad
                    kokku="".join(vajalik)
                else:
                    continue
            kokku="".join(kokku)
        else:
            kokku=kokku+laps+": "+üks+"\n"
        üks=""
        teine=""
        g2.close()
    return kokku
    g1.close()
    

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
