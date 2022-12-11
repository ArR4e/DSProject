from film import loetleFilmid, lisaFilm, kustutaFilm

def töötleKäsk(tähis, sisend = []):
    if tähis == 'K':
        if len(loetleFilmid(sisend[0])) == 0:
            print("Antud zanriga filme saadaval pole, valige uuesti")
        else:
            print("Võimalikud filmid on:", (*loetleFilmid(sisend[0])), sep = "\n")
        
    if tähis == 'L':
        lisaFilm(sisend[1], sisend[0])
        print("Film lisatud!")
    if tähis == 'V':
        kustutaFilm(sisend[0])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        
while True:
    o = input()
    if o[0] == 'K':
        o = o.split()
        taht = o.pop(0)
        töötleKäsk(taht, o)
    if o[0] == 'L':
        o = o.split(" ", 2)
        taht = o.pop(0)
        töötleKäsk(taht, o)
    if o[0] == 'V':
        o = o.split(" ", 1)
        taht = o.pop(0)
        töötleKäsk(taht, o)
    if o[0] == 'E':
        break