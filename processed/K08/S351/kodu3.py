import film

def töötleKäsk(tähis,järjend):
    if tähis=="K":
        print("Võimalikud filmid on:")
        film.loetleFilmid(järjend[1])
        return True
    elif tähis=="L":
        filmi_nimi=järjend[2:]
        filmikene=""
        for el in filmi_nimi:
            filmikene+=el
            filmikene+=" "
        filmikene=filmikene[:-1]
        film.lisaFilm(filmikene,järjend[1])
        print("Film lisatud!")
        return True
    elif tähis == "V":
        filmi_nimi=järjend[1:]
        filmikene=""
        for el in filmi_nimi:
            filmikene+=el + " "
        filmikene=filmikene[:-1]
        film.kustutaFilm(filmikene)
        print("Film nimekirjas kustutatud!")
        print("Head vaatamist!")
        return True
    else:
        return False

#Sisend kasutajalt
while True:
    sisend_kasutajalt=input()
    järjend=[]
    järjend.append(sisend_kasutajalt)
    järjend = (järjend[0].split())
    if järjend[0]!="E":
        töötleKäsk(järjend[0], järjend)
    else:
        break



    
