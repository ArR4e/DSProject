# Failis lapsed.txt on igal real vanema isikukood, tühik ja lapse isikukood.
# Failis nimed.txt on igal real ühe inimese isikukood, tühik ja tema nimi. Võib eeldada,
# et korduvaid nimesid failis ei esine. Samuti võib eeldada, et iga failis lapsed.txt oleva
# isikukoodi jaoks on failis nimed.txt välja toodud vastav nimi.
# 
# Kirjuta programm, mis väljastab ekraanile iga lapse kohta ühe rea: nimi, koolon, tühik
# ning seejärel koma ja tühikuga eraldatuna ema ja isa nimi. Kui teada on ainult üks vanem,
# siis väljastada ainult see. Näiteks antud failide korral peaksid ekraanile ilmuma
# järgnevad read (laste ega nende vanemate järjekord pole tähtis):
#  Robert Peedumets: Madli Peedumets, Peeter Peedumets
#  Maria Peedumets: Madli Peedumets, Peeter Peedumets
#  Liisa-Maria Jaaniste: Kadri Kalkun
#  Peeter Peedumets: Karl Peedumets
# Põhitöö tuleks delegeerida funktsioonile seosta_lapsed_ja_vanemad, mille
# parameetriteks on laste faili nimi ja nimede faili nimi ning mis tagastab sõnastiku,
# kus kirje võtmeks on lapse nimi ja väärtuseks tema vanemate nimede hulk.
# 
# Näiteks antud failide korral peaks tulemus olema järgmine:
# 
# >>> seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
# {'Robert Peedumets': {'Madli Peedumets', 'Peeter Peedumets'}, 'Maria Peedumets': {'Madli Peedumets', 'Peeter Peedumets'},
# 'Liisa-Maria Jaaniste': {'Kadri Kalkun'}, 'Peeter Peedumets': {'Karl Peedumets'}}
# Automaatkontroll. Programm ei tohiks kasutajalt midagi küsida. Andmefailide nimed lapsed.txt ja nimed.txt peaksid olema
# kirjutatud programmi sisse, st põhiprogramm pöördub nendega funktsiooni seosta_lapsed_ja_vanemad poole.



def seosta_lapsed_ja_vanemad(lapsedfail, nimedfail):
    lapsed = open(lapsedfail)
    nimed = open(nimedfail)
    isik_nimi = {}
    isikud2 = {}
    seostatudlapjavan = {}
    for rida in nimed:
        nimi_isik = rida.split()
        nimi = nimi_isik[1] + " " + nimi_isik[2]
        isik_nimi[nimi_isik[0]] = nimi
        #sonastik[key] = value        
    for rida in lapsed:
        isikud = rida.split()
        isikudvan = isikud[0]
        isikudlap = isikud[1]
        if isikudlap in isikud2.keys():
            isikud2[isikudlap] = (isikud2[isikudlap],isikudvan)
        else:
            isikud2[isikudlap] = isikudvan            
    for l,v in isikud2.items():
        laps_nimi = isik_nimi[l]
        vanemate_nimid = set()
        if len(v) == 11:
            x = isik_nimi[v]
            vanemate_nimid.add(x)
        else:
            van1,van2 = v
            vanemate_nimid.add(isik_nimi[van1])
            vanemate_nimid.add(isik_nimi[van2])
        seostatudlapjavan[laps_nimi] = vanemate_nimid

    return seostatudlapjavan

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
        
            