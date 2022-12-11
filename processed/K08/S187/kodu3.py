from film import loetleFilmid, lisaFilm, kustutaFilm

def töötleKäsk(kask, argument):
    if kask == "K":
        print(loetleFilmid(argument[0]))
        print("Selliseid filme pole, tee uus valik.")
        return(True)
    elif kask == "L":
        lisaFilm(argument[1], argument[0])
        return(True)
    elif kask == "V":
        kustutaFilm(argument[0])
        return(True)
    else:
        return(False)
    
while True:
    sis = input().split(" ")
    töötleKäsk(sis[0], sis[1])
    if not töötleKäsk(sis[0], sis[1]):
        break