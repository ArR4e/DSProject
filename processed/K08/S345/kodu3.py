import film

def töötleKäsk(käsu_tähis, käsu_argumendid):
    if käsu_tähis == "K":
        print("Võimalikud filmid on:")
        filmid = film.loetleFilmid(käsu_argumendid[0])
        for el in filmid:
            print(el)
    elif käsu_tähis == "L":
        film.lisaFilm(käsu_argumendid[1], käsu_argumendid[0])
        print("Film lisatud!")
    elif käsu_tähis == "V":
        film.kustutaFilm(käsu_argumendid[0])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
    elif käsu_tähis == "E":
        return False
    else:
        print("Sellist käsku ei ole")

print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi pealkiri>\nLõpeta:      E\n===\n")

while True:
    sisend = input("> ")
    
    if sisend == "E":
        break
    
    käsk = sisend[0]
    žanr = ""
    pealkiri = ""
    n = 0
    järjend = []

    if käsk == "K":
        žanr = sisend[2:]
        järjend.append(žanr)
    elif käsk == "L":
        for t in sisend[2:]:
            if t == " ":
                n += 1
                break
            else:
                žanr += (t)
                n += 1
        pealkiri = sisend[2+n:]
        järjend = [žanr, pealkiri]
    elif käsk == "V":
        pealkiri = sisend[2:]
        järjend.append(pealkiri)
    else:
        järjend = []

    töötleKäsk(käsk, järjend)