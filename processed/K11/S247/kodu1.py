def seosta_lapsed_ja_vanemad(lfail, nfail):
    tulemus = {}
    järjend = []
    with open(nfail, "r", encoding="UTF=8") as f:
        for rida in f:
            ikood, nimi = rida.strip().split(" ",1)
            järjend.append((nimi, ikood))
    
    with open(lfail, "r", encoding="UTF=8") as f:
        for rida in f:
            vanem, laps = rida.strip().split(" ",1)
            for element in järjend:
                if vanem == element[1]:
                    vanemaNIMI = element[0]
                elif laps == element[1]:
                    lapseNIMI = element[0]
            if lapseNIMI not in tulemus:
                tulemus[lapseNIMI] = set([vanemaNIMI])
            else:
                t = list(tulemus[lapseNIMI])
                t.append(vanemaNIMI)
                t = set(t)
                tulemus[lapseNIMI] = t
    return tulemus
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))

            
    
    



         
    
    
    
    
    
