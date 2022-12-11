# Failis filmid.txt on nimekiri filmidest kood nende žanritega järgneval kujul,kus igal real on tühikute ja
# sidekriipsuga (' - ') eraldatult filmi nimi ja žanr. Üks faili filmid.txt võimalik sisu oleks:
# Shrek - multikas
# Avengers: End Game - märul
# The Quiet Place - õudukas
# Spider-Man - märul
# Moana - multikas
# The Conjuring 3 - õudukas
# Et nimekirja oleks võimalik mugavalt täiendada, koosta selle jaoks Pythoni fail film.py ning kirjuta
# sinna järgmised funktsioonid:
# Funktsioon loetleFilmid, mis võtab argumendiks žanri nime ning tagastab järjendi kõikide filmide
# nimedega, mis on etteantud žanrist.
# Funktsioon lisaFilm, millel on kaks argumenti. Esimeseks argumendiks on nimi ning teiseks žanr.
# Funktsioon peab olemasolevasse faili filmid.txt soovitud filmi koos žanriga lisama kujul nimi - žanr,
# näiteks Spider-Man - märul.
# Funktsioon kustutaFilm, mis võtab argumendiks filmi nime ning kustutab selle olemasolevast tekstifailist ära.
# Funktsioon loetleFilmid peab ülaloleva näitefaili filmid.txt puhul käituma järgmiselt:
# >>> loetleFilmid("märul")
# ['Avengers: End Game', 'Spider-Man']
# Automaatkontroll. Programmifaili nimi peab olema film.py. Funktsioonil loetleFilmid peab olema üks
# parameeter - žanri nimetus, mis on sõne. Funktsioon avab faili filmid.txt ja tagastab sobivate filmide nimede järjendi.
# Filmide järjekord selles ei ole oluline, aga järjend peab sisaldama parajasti kõigi sobivate filmide nimesid.
# Funktsioonil lisaFilm peab olema kaks parameetrit: filmi nimi ja žanri nimetus, mis on mõlemad sõned.
# Funktsioon avab faili filmid.txt ja kirjutab sinna uue rea sobival kujul. Funktsioonil kustutaFilm peab olema üks
# parameeter: filmi nimi, mis on sõne. Funktsioon avab faili filmid.txt ja eemaldab sealt rea, kus on kirjas vastav film.
def uusfilminimi():
    file = open('filmid.txt','r')
    divided = file.split('\n')
    nimi = []
    quantity = len(divided)
    for i in quantity:
        x = divided[i]
        x = x.split('-')
        normalname += x
    file.close()
def loetleFilmid(kind):
    x = uusfilminimi()
    uuednimed = []
    try:
        zanr = x.index(kind) - 1
        film = x[zanr]
        
    
    
