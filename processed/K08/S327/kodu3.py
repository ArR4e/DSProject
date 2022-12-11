import film
def töötleKäsk(tähis, argumendid):
    if tähis == "K":
        print(film.loetleFilmid(argumendid[0]))
        return True
    elif tähis == "L":
        asd = argumendid[0].split(" ", 1)
        film.lisaFilm(asd[1],asd[0])
        return True
    elif tähis == "V":
        film.kustutaFilm(argumendid[0])
        return True
    elif tähis == "E":
        return False
    
while True:
    käsk = [input(),[input()]]
    if töötleKäsk(käsk[0],käsk[1]) == False:
        break
    else:
        töötleKäsk(käsk[0],käsk[1])