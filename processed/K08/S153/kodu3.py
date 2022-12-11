import film

print("====== FILMIANDMEBAAS ======\nKuva filmid: K <žanr>\nLisa film:   L <žanr><film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===========================\n")
input = input()
a = list(input.split(" "))

if len(a) == 2:
    tähis = a[0]
    sisend = a[1]
elif len(a) == 3:
    tähis = a[0]
    nimi = a[2]
    zanr = a[1]
    sisend1 = [nimi, zanr]
    sisend = ", ".join([str(el)for el in sisend1])
elif len(a) == 1:
    tähis = a[0]
    
def töötleKäsk():
    if tähis == "K":
        tulemus = film.loetleFilmid(sisend)
        print("Võimalikud filmid on: \n" + "\n".join([str(el)for el in tulemus]))
        return True
    elif tähis == "L":
        tulemus = film.lisaFilm(nimi, zanr)
        print("Film lisatud!")
        return True
    elif tähis == "V":
        tulemus = film.kustutaFilm(sisend)
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    elif tähis == "E":
        return False
