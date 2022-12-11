import film

def töötleKäsk(käsk, valikud):
    filminimi = ""
    if käsk in valikud:
        if käsk == valikud[0]:
            zanr = käsklus[1]
            print(zanr)
            film.loetleFilmid(zanr)
            print(film.filminimi)
            return True
        elif käsk == valikud[1]:
            zanr = käsklus[1]
            filmnimi = käsklus[2::]
            for elem in filmnimi:
                filminimi += elem + " "
            filminimi = filminimi.capitalize()
            film.lisaFilm(filminimi, zanr)
            return True
        elif käsk == valikud[2]:
            filmnimi = käsklus[1::]
            for elem in filmnimi:
                filminimi += elem + " "
            film.kustutaFilm(filminimi)
            return True
        elif käsk == valikud[3]:
            return False

            
while True:
    valikud = ["K", "L", "V", "E"]
    käsklus = input("K, L, V või E: ").capitalize().split(" ")
    käsk = käsklus[0]
    if töötleKäsk(käsk, valikud) == False:
        break
    
