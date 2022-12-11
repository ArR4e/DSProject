#päris pikk ja kole sai, aga iseenesest peaks toimima; kahjuks automaatkontrollile ei meeldi midagi :(
with open("lapsed.txt") as flapsed, open("nimed.txt") as fnimed:

    def seosta_lapsed_ja_vanemad(flapsed, fnimed):
        uus = {}
        uus2 = []
        uus3 = {}
        indeks = 0
        #siin salvestab programm nime ja isikukoodi sõnastikku "uus"
        for rida in fnimed:
            järjend = rida.split(" ")
            kood = järjend[0]
            nimi = järjend[1] + " " + järjend[2]
            uus[kood] = nimi.strip("\n")
        #nüüd teeme järjendi, kus lapse nimele järgneb ta vanema nimi, millele järgneb uus lapse nimi jne
        for rida in flapsed:
            tühi = {}
            järjend2 = rida.strip().split()
            if järjend2[1] in uus:
                tühi[uus[järjend2[1]]] = set([uus[järjend2[0]]])
                uus2.append(uus[järjend2[1]])
                uus2.append(uus[järjend2[0]])
            else:
                continue
        #siin moodustame järjendist sõnastiku, kus lapsele vastavad ta vanemate nimed
        for element in uus2:
            if indeks % 2 != 0:
                indeks += 1
            elif uus2[indeks] not in uus3:
                uus3[element] = set([uus2[indeks + 1]])
                indeks += 1
            else:
                uus3[element] = set([" ".join(uus3[element]) + ", "+ uus2[indeks + 1]])
                indeks += 1
        return uus3
            
    tagastus = seosta_lapsed_ja_vanemad(flapsed, fnimed)
    for laps in tagastus:
        print(laps + ": " + " ".join(tagastus[laps]))
    
