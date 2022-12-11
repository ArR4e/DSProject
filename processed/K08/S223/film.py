def loetleFilmid(žanr):
    with open("filmid.txt", "r") as f:
        list_films = f.readlines()
        list_films = [film.strip().split(" - ") for film in list_films]
    return [films[0] for films in list_films if films[1] == žanr]

def lisaFilm(nimi, žanr):
    with open("filmid.txt", "r") as f:
        rida = f.readlines()
    with open("filmid.txt", "a+") as f:
        if rida != []:
            f.write("\n" + nimi + " - " + žanr)
        else:
            f.write(nimi + " - " + žanr)

def kustutaFilm(nimi):
    with open("filmid.txt", "r") as f:
        list_films = f.readlines()
        list_films = [film.strip().split(" - ") for film in list_films]
    with open("filmid.txt", "w") as f:
        for film in list_films:
            if film[0] != nimi:
                f.write(film[0] + " - " + film[1] + "\n")