import film


def töötleKäsk(käsk, jär):
        if käsk == "K":
            sobivadfilmid = film.loetleFilmid(jär[0])
            print(f"Sobivad filmid on:\n")
            for i in sobivadfilmid:
                print(i)
            return True
        elif käsk == "L":
            film.lisaFilm(" ".join(jär[1:]), jär[0])
            print("Film lisatud!")
            return True
        elif käsk == "V":
            film.kustutaFilm(jär[0])
            print("Film kustutatud")
            return True
        elif käsk == "E":
            return False
while True:
        sisend = input("").split(" ")
        käsk = sisend[0]
        jär = sisend[1:]
        töötleKäsk(käsk, jär)
        if käsk == "E":
            break