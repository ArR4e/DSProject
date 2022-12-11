# 1. Lapsed ja vanemad
# Failis lapsed.txt on igal real vanema isikukood, tühik ja lapse isikukood.
# Failis nimed.txt on igal real ühe inimese isikukood, tühik ja tema nimi.
# Võib eeldada, et korduvaid nimesid failis ei esine. Samuti võib eeldada, et iga failis lapsed.txt
# oleva isikukoodi jaoks on failis nimed.txt välja toodud vastav nimi.

# Kirjuta programm, mis väljastab ekraanile iga lapse kohta ühe rea: nimi, koolon, tühik
# ning seejärel koma ja tühikuga eraldatuna ema ja isa nimi. Kui teada on ainult üks vanem,
# siis väljastada ainult see. Näiteks antud failide korral peaksid ekraanile ilmuma järgnevad read
 #(laste ega nende vanemate järjekord pole tähtis):

# Robert Peedumets: Madli Peedumets, Peeter Peedumets
# Maria Peedumets: Madli Peedumets, Peeter Peedumets
# Liisa-Maria Jaaniste: Kadri Kalkun
# Peeter Peedumets: Karl Peedumets

# Põhitöö tuleks delegeerida funktsioonile seosta_lapsed_ja_vanemad,
# mille parameetriteks on laste faili nimi ja nimede faili nimi ning mis tagastab sõnastiku,
# kus kirje võtmeks on lapse nimi ja väärtuseks tema vanemate nimede hulk.

# Näiteks antud failide korral peaks tulemus olema järgmine:

# >>> seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
# {'Robert Peedumets': {'Madli Peedumets', 'Peeter Peedumets'}, 'Maria Peedumets': {'Madli Peedumets', 'Peeter Peedumets'}, 'Liisa-Maria Jaaniste': {'Kadri Kalkun'}, 'Peeter Peedumets': {'Karl Peedumets'}}
# Automaatkontroll. Programm ei tohiks kasutajalt midagi küsida.
# Andmefailide nimed lapsed.txt ja nimed.txt peaksid olema kirjutatud programmi sisse,
# st põhiprogramm pöördub nendega funktsiooni seosta_lapsed_ja_vanemad poole.


#koodid = "lapsed.txt"
#nimed = "nimed.txt"

def seosta_lapsed_ja_vanemad(koodid, nimed):
    # 
    f_nimed = open(nimed)
    d1 = {}
    for rida in f_nimed:
        andmed = rida.strip().split()
        d1[andmed[0]] = d1.get(andmed[0], (str(andmed[1] + " " + andmed[2])))
    f_nimed.close()

    # lapsed ja vanemad
    f_koodid = open(koodid)
    d2 = {}
    for rida in f_koodid:
        andmed = rida.strip().split()
        
        if andmed[1] in d1.keys():
            laps = d1[andmed[1]]
            
        if andmed[0] in d1.keys():
            vanem = d1[andmed[0]]
        
        if laps not in d2:
            d2[laps] = set()
            d2[laps].add(vanem)
        else:
            d2[laps].add(vanem)
    f_koodid.close()
    
    return d2


