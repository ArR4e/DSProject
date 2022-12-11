from collections import defaultdict

def seosta_lapsed_ja_vanemad(fail1, fail2):
    with open(fail1, "r") as f:
        #{laps: vanem}
        idd = defaultdict(list) 
        for el in f:
            el=el.split()
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
        #kui id lapse oma
        #print(num, nimi)
        if num in idd.keys():
            vanemadId = [idd[el] for el in idd.keys() if el == num]
            #print(vanemadId)
            vanemad= set()
            for el in vanemadId:
                if (type(el) == list):
                   for i in el:
                        #print(i)
                        #print(d[i])
                        vanemad.add(d[i])
                else:
                    vanemad.add(d[el])
                    #print(el)
            #print(vanemad)
            lõpuTabel[nimi] = vanemad 
    return lõpuTabel
        
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))

