from collections import defaultdict

def seosta_lapsed_ja_vanemad(fail1, fail2):
    with open(fail1, "r") as f:
        #{laps: vanem}
        idd = defaultdict(list)
        for el in f:
            el = el.split()
            el[1] = el[1].strip()
            idd[el[1]].append(el[0])
    print(idd)
    
    with open(fail2, "r") as f:
        d = {}
        for rida in f:
            asjad = rida.split()
            d[asjad[0]] = " ".join(asjad[1:])
        print(d)
        
    lõpuTabel = {}
    
    for num, nimi in d.items():
        if num in idd.keys():
            vanemadId = [idd[el] for el in idd.keys() if el == num]
            vanemad = set()
            for el in vanemadId:
                if (type(el) == list):
                    for i in el:
                        vanemad.add(d[i])
                else:
                    vanemad.add(d[el])
                    
            lõpuTabel[nimi] = vanemad
    return lõpuTabel

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
