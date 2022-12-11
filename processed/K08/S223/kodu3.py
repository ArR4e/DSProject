import film

def töötleKäsk(letter, variable):
    if letter == "K":
        for films in film.loetleFilmid(variable):
            print(films)
        return True
    elif letter == "L":
        print("Film lisatud!")
        splitting = variable.index(" ")
        film.lisaFilm(variable[splitting+1:], variable[:splitting])
        return True
    elif letter == "V":
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        film.kustutaFilm(variable)
        return True
    elif letter == "E":
        return False



käsk = input("> ")
käsk = [käsk[0],käsk[2:]]
while töötleKäsk(käsk[0], käsk[1]):
    käsk = input("> ")
    käsk = [käsk[0],käsk[2:]]

