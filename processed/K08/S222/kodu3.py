import film

def töötleKäsk(t,l):
    if t == "K":
        print("Võimalikud filmid on: ")
        filmid = film.loetleFilmid(l[0])
        for f in filmid:
            print(f)
    elif t == "L":
        film.lisaFilm(l[1],l[0])
        print("Film lisatud!")
    elif t == "V":
        film.kustutaFilm(l[0])
        print("Film nimekirjast kustutatud!")
    elif t == "E":
        return False

print("===FILMIANDMEBAAS===")
print("Kuva filmid: K <žanr>")
print("Lisa film: L <žanr> <film>")
print("Vaata filmi: V <fili nimi>")
print("Lõpeta: E")
print("===")

e = True
while e or e == None:
    sisend = input("")
    if sisend[0] == "E":
        e = False
        break
    if sisend[0] == "L":
        järel = sisend[1:]
        järel = järel.split()
        l1 = järel[0]
        järel.remove(l1)
        l = " ".join(järel)
        sisend = [sisend[0],[l1,l]]
    else:
        sisend = [sisend[0],sisend[1:]]
        järel = sisend[1].lstrip()
        sisend = [sisend[0],[järel]]
    e = töötleKäsk(sisend[0],sisend[1])