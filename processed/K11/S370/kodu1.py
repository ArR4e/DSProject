def seosta_lapsed_ja_vanemad(lapsed, nimed):
    fnimed=open(nimed, "r")
    flapsed=open(lapsed, "r")
    
    andmed={}
    
    vastavus={}
    for rida in fnimed:
        kood=rida[:rida.index(' ')]
        nimi=rida[rida.index(' ')+1:].strip()
        vastavus[kood]=nimi
    
    
    for rida in flapsed:
        lapskood=rida[rida.index(' ')+1:].strip()
        vanemkood=rida[:rida.index(' ')]
        laps=vastavus[lapskood]
        vanem=vastavus[vanemkood]
        if laps not in andmed:
            andmed[laps]=set()
            andmed[laps].add(vanem)
        else:
            andmed[laps].add(vanem)
            
    return(andmed)
            
seos=seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for laps in seos:
    vanemad=", ".join(seos[laps])
    print(laps+": "+vanemad)
    