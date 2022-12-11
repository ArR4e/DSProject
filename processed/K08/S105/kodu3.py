import film

def töötleKäsk(a,b):
    if a == "K":
        print("Võimalikud filmid on: ")
        filmid=film.loetleFilmid(b[0])
        for ele in filmid:
            print(ele)
        return True
    if a == "L":
        zanr=b[0]
        b.remove(b[0])
        b=(" ".join(b))
        film.lisaFilm(b,zanr)
        print("Film lisatud!")
        return True
    if a == "V":
        film.kustutaFilm(b[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    if a == "E":
        return False

while True:
    sisend=[]
    sisse=input()
    sisend=sisse.split(" ")
    ksk=sisend[0]
    sisend.remove(sisend[0])    
    if töötleKäsk(ksk,sisend)==False:
        break