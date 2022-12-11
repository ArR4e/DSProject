def seosta_lapsed_ja_vanemad(lapsed,nimed):
    f1=open(lapsed,encoding="UTF-8")
    f2=open(nimed,encoding="UTF-8")
    sõnastik={}
    nimed={}
    for rida in f2:
        nimed[rida.split()[0]]=" ".join(rida.split()[1:])
    for rida in f1:
        laps=rida.split()[1]
        vanem=rida.split()[0]
        vanemad=sõnastik.get(nimed[laps],set())
        vanemad.add(nimed[vanem])
        sõnastik[nimed[laps]]=vanemad
    f1.close()
    f2.close()
    return sõnastik
