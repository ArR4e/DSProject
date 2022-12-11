import film
def töötleKäsk(tähis, film):
    sisend=input("Kirjuta sisend: ")
    järjend=sisend.split()
    tähis=järjend[0]
    n=1
    film=[]
    while n < len(järjend):
        sisu=järjend[n]
        film += [sisu]
        n += 1
        töötleKäsk(tähis, film)
        if tähis == "K":
            teema=film[0]
            vaata=filmid.loetleFilmid(teema)
            print ("Võimalikud filmid on: ")
            n=0
            while n < len(vaata):
                print (vaata[n])
                n += 1
                return True
        elif tähis == "L":
            nimi=film[1]
            teema=film[0]
            vaata=filmid.lisaFilmid(nimi, teema)
            print ("Film lisatud!")
            return True
        elif tähis == "V":
            nimi=film[0]
            vaata=filmid.kustutaFilmid(nimi)
            print ("Film nimekirjast kustutatud!")
            print ("Head vaatamist!")
            return True
        elif tähis == "E":
            return False
