filmid = open("filmid.txt", "rt", encoding = "utf-8")
kõik_filmid = []
for rida in filmid:
    kõik_filmid.append(rida.strip())
filmid.close()

filmid_list = []
filmid_žanr_list = []
for rida in kõik_filmid:
    uus_list = rida.split(" - ")
    filmid_list.append(uus_list[0])
    filmid_žanr_list.append(uus_list[1])
    
#print(filmid_list)
#print(filmid_žanr_list)

#defineerib loetleFilmid
def loetleFilmid(žanr):
    filmivalikud = []
    for i in range(len(filmid_žanr_list)):
        if filmid_žanr_list[i] == žanr:
            filmivalikud.append(filmid_list[i])
    return filmivalikud
#print(loetleFilmid("õudukas"))

#lisab filmi koos žanriga algfaili
def lisaFilm(film, žanr):
    filmid = open("filmid.txt","at", encoding = "utf-8")
    lisatav_rida = str("\n" + film + " - " + žanr)
    filmid.write(lisatav_rida)
    filmid.close()
#print(lisaFilm("The Godfather","kuld"))


#kustutab filmi failist
def kustutaFilm(film):
    filmid = open("filmid.txt","rt", encoding = "utf-8")
    read = filmid.readlines()
    filmid.close()
    for rida in read:
        if rida.startswith(film):
            del read[read.index(rida)]
    filmid = open("filmid.txt","wt", encoding = "utf-8")
    for i in read:
        filmid.write(i)
    filmid.close()
#print(kustutaFilm("Moana"))
    

