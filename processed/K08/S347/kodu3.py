import film
print("+---FILMIANDMEBAAS---+")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
def töötleKäsk(tähis,järjend):
    while True:
        sisend = str(input(">")).split()
        tähis = sisend[0]
        if tähis == "K":
            žanr = sisend[1].strip("\n")
            loetelu = film.loetleFilmid(žanr)
            for i in range(len(loetelu)):
                print(loetelu[i])
        if tähis == "L":
            žanr = sisend[1].strip("\n")
            if len(sisend)== 3:
                nimi= sisend[2]
                film.lisaFilm(nimi, žanr)
            if len(sisend)== 4:
                nimi= sisend[2]+" "+sisend[3]
                film.lisaFilm(nimi, žanr)
            if len(sisend)== 5:
                nimi= sisend[2]+" "+sisend[3]+" "+sisend[4]
                film.lisaFilm(nimi, žanr)
            print("Film lisatud!")
        if tähis == "V":
            filminimi = sisend[1].strip("\n")
            film.kustutaFilm(filminimi)
            print("Film nimekirjast kustutatud!")
            print("Head vaatamist!")
        if tähis == "E":
            break
    if tähis != "E":
        return True
    else:
        return False
töötleKäsk("tähis","järjend")
