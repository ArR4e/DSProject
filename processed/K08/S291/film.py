def loetleFilmid(žanr):
    žanri_indeksid = []
    žanri_järjend = []
    for indeks in range(len(filmid2)):
        if filmid2[indeks] == žanr:
            žanri_indeksid += [indeks]
    for indeks in range(len(žanri_indeksid)):
        žanri_järjend += [filmid2[žanri_indeksid[indeks]-1]]
    return žanri_järjend

def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a", encoding = "UTF-8")
    fail.write("\n" + nimi + " - " + žanr)
    fail.close()
    
def kustutaFilm(nimi):
    fail = open("filmid.txt", encoding = "UTF-8")
    uus_järjend = []
    for rida in fail:
        if nimi not in rida:
            uus_järjend += [rida]
    fail.close()
    fail = open("filmid.txt", "w", encoding = "UTF-8")
    for element in uus_järjend:
        fail.write(element)
    fail.close()
            

fail = open("filmid.txt", encoding = "UTF-8")
filmid1 = []
filmid2 = []

for rida in fail:
    rida = rida.split(" - ")
    filmid1 += rida
for element in filmid1:
    if element.endswith("\n"):
        filmid2 += element.split()
    else:
        filmid2 += [element]

fail.close()