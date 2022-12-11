def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    with open(nimedefailinimi, encoding = "UTF-8") as fail:
        isiknimi = {}
        for rida in fail:
            rida = rida.strip().split(" ")
            isiknimi[rida[0]] = " ".join(rida[1:])
    
    with open(lastefailinimi, encoding = "UTF-8") as fail:
        sugulus = []
        lapsed = {}
        for algrida in fail:
            algrida = algrida.strip().split(" ")
            rida = []
            for element in algrida:
                rida += [isiknimi[element]]
            if rida[1] not in lapsed:
                lapsed[rida[1]] = len(sugulus)
                sugulus += [[rida[1], rida[0]]]
            else:
                sugulus[lapsed[rida[1]]] += [rida[0]]
        for i in range(0,len(sugulus)):
            sugulus[i] = [sugulus[i][0],set(sugulus[i][1:])]
            
            
        return dict(sugulus)
nimistu = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")  
for element in nimistu:
    print(f"""{element}: {str(nimistu[element])[1:-1].replace("'","")}""")