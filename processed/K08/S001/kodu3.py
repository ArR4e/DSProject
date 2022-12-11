import film

def töötleKäsk(taht,argumendid):
    if taht == "K":
        print("Võimalikud filmid on: ")
        for filminimi in film.loetleFilmid(argumendid[0]):
            print(filminimi)
    if taht == "L":
        film.lisaFilm(argumendid[1], argumendid[0])
        print("Film lisatud!")
    if taht == "V":
        film.kustutaFilm(argumendid[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    if taht == "E":
        return False
    return True

print("====== FILMIANDMEBAAS ======")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("============================")

jatka = True
while jatka == True:
    andmed = input()
    andmed = andmed.split(" ", 1)
    argumendid = []
    if andmed[0] == "L":
        argumendid.extend(andmed[1].split(" ", 1))
    elif andmed[0] == "K" or andmed[0] == "V":
        argumendid.append(andmed[1])
    taht = andmed[0]
    jatka = töötleKäsk(taht, argumendid)