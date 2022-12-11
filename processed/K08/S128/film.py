#Filmide nimekiri
fail = open("filmid.txt", encoding="UTF-8")
filmid = []
for rida in fail:
    filmid += rida.strip().split(" - ")
fail.close()

def loetleFilmid(žanr):
    films_genre = []
    for i in range(1, len(filmid), 2):
        if filmid[i] == žanr:
            films_genre += [filmid[i-1]]
    return films_genre
            
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", encoding="UTF-8", mode="r")
    filmid_list = []
    for rida in fail:
        filmid_list += rida.strip().split(" - ")
    fail.close()
    fail = open("filmid.txt", encoding="UTF-8", mode="a+")
    if filmid_list == []:
        fail.write(nimi + " - " + žanr)
    else:
        fail.write("\n" + nimi + " - " + žanr)
    fail.close()
    
def kustutaFilm(nimi):
    fail = open("filmid.txt", encoding="UTF-8", mode="r")
    filmid_list = []
    for rida in fail:
        filmid_list += rida.strip().split(" - ")
    fail.close()
    fail = open("filmid.txt", encoding="UTF-8", mode="w")
    for i in range(0, len(filmid_list), 2):
        if filmid_list[i] != nimi:
            fail.write(filmid_list[i] + " - " + filmid_list[i+1] + "\n")
    fail.close()