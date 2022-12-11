def seosta_lapsed_ja_vanemad(lapsed, nimed):
    sonastik = {}
    lapse_sonastik = {}
    inimesed = []
    isikud = []
    with open(lapsed) as lapsed:
        with open(nimed) as nimed:
            for rida in lapsed:
                rida = rida.split()
                for isik in rida:
                    isik = int(isik)
                    isikud.append(isik)
            for rida in nimed:
                rida = rida.split(" ", 1)
                number = 0
                for isik_nimi in rida:
                    if number == 0:
                        isik_nimi = int(isik_nimi)
                    elif number == 1:
                        isik_nimi = isik_nimi.strip()
                    inimesed.append(isik_nimi)
                    number += 1
            for isik in range(0, len(inimesed), 2):
                sonastik[inimesed[isik]] = inimesed[isik + 1]
            for isik in range(0, len(isikud), 2):
                vanemad = set()
                vanemad.add(sonastik[isikud[isik]])
                if sonastik[isikud[isik + 1]] in lapse_sonastik:
                    lapse_sonastik[sonastik[isikud[isik + 1]]].add(sonastik[isikud[isik]])
                else:
                    lapse_sonastik[sonastik[isikud[isik + 1]]] = vanemad
                    
            return lapse_sonastik
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))