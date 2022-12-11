import film

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        rida=film.loetleFilmid(järjend[0])
        print(f"Võimalikud filmid on:\n {rida}")
        return True
    elif tähis == "L":
        zanr=järjend[0]
        pealkiri=järjend[1:]
        pealkiri=" ".join(pealkiri)
        film.lisaFilm(pealkiri, zanr)
        return True
    elif tähis =="V":
        film.kustutaFilm(" ".join(järjend))
        print("Film nimekirjast kustutaud! \n Head vaatamist")
        return True
    else:
        return False
    
x=True
while x==True:
    sisend=input()
    sisend=sisend.split(" ")
    x=töötleKäsk(sisend[0],sisend[1:])
    

