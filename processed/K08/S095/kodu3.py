import film
with open("tervitus.txt", encoding = 'utf-8') as f:
    print(f.read())
while True:
    print("\n")
    sisestus=input(">")
    sisestus = sisestus.split()
    käsk=sisestus[0]
    if käsk == "K":
        järjend=sisestus[1]
        def töötleKäsk(käsk, järjend):
                print("Võimalikud filmid on:")
                for i in film.loetleFilmid(järjend):
                    print(i)
        töötleKäsk(käsk, järjend)
    elif käsk == "L":
        järjend=sisestus[1]
        def töötleKäsk(käsk, järjend):
            filminimi=sisestus[2:]
            filminimi=' '.join(filminimi)
            film.lisaFilm(filminimi, järjend)
            print("Film lisatud!")
        töötleKäsk(käsk, järjend)
    elif käsk == "V":
        järjend=sisestus[1:]
        järjend=' '.join(järjend)
        def töötleKäsk(käsk, järjend):
            nimi=järjend
            film.kustutaFilm(nimi)
            print("Film nimekirjast kustutatud!")
            print("Head vaatamist!")
        töötleKäsk(käsk, järjend)
    elif käsk == "E":
        break
        
            