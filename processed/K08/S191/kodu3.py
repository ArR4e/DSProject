import film

print("_-_-FILMID-_-_\nKuva filmid:  K [žanr]\nLisa film:    L [žanr,nimi]\nVaata filmi:  V [nimi]\nExit:         E\n--------------")

def töötleKäsk(tähis, täpsustus):
    if tähis=="K":
        if film.loetleFilmid(täpsustus[0])==[]:
            print("Selliseid filme pole!")
        else:
            print("Valikus on:")
            for i in film.loetleFilmid(täpsustus[0]):
                print(i)
        return True
    elif tähis=="L":
        film.lisaFilm(täpsustus[1],täpsustus[0])
        print("Film lisatud!")
        return True
    elif tähis=="V":
        film.kustutaFilm(täpsustus[0])
        print("Film nimekirjast eemaldatud. Head vaatamist!")
        return True
    elif tähis=="E":
        return False

loop=True
while loop:
    sisend=input(">")
    split_sisend=sisend.split(" ")
    if split_sisend[0]=="L":
        filmi_nimi=" ".join(split_sisend[2:])
        film_käsus=[split_sisend[1]]+[filmi_nimi]
        loop=töötleKäsk(split_sisend[0],film_käsus)
    elif split_sisend[0]=="V":
        filmi_nimi=" ".join(split_sisend[1:])
        loop=töötleKäsk(split_sisend[0],[filmi_nimi])
    elif split_sisend[0]=="K":
        loop=töötleKäsk(split_sisend[0], [split_sisend[1]])
    else:
        loop=töötleKäsk(split_sisend[0],[])