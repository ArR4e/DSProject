import film

def töötleKäsk(käsk, arg):
    if käsk == "K":
        filmid = ""
        for n in arg:
            filmu = film.loetleFilmid(n)
        for e in filmu:
            filmid += str(e)+"\n"
        if filmid == "":
            print("Selle žanriga pole ühtegi filmi")
        else:
            print("Võimalikud filmid on:\n" +filmid)
        return True
    if käsk == "V":
        nimi = arg
        o = " "
        o = o.join(arg)
        film.kustutaFilm(o)
        print("Film nimekirjast kustutatud!\n Head vaatamist!")
        return True
    if käsk == "L":
        fnimi = arg[1:]
        l = " "
        l = l.join(fnimi)
        film.lisaFilm(l, arg[0])
        print("Film lisatud!")
        return True
    elif käsk == "E":
        return False
      
while True:
    käsk = str(input(">")) 
    käsk = käsk.split(" ")
    arg = käsk[1:]
    vastus = töötleKäsk(käsk[0], arg)
    if vastus == True:
        continue
    else:
        break
    