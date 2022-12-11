import film

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        if len(film.loetleFilmid(y)) == 0:
            print("Sellise žanriga filme pole failis.")
            return True
        else:
            print("Võimalikud filmid on: \n" + "\n".join(map(str, film.loetleFilmid(y))))
            return True
    elif tähis == "L":
        uus_y = y.split()
        y_žanr = uus_y[0]
        y_filmi_nimi = " ".join(uus_y[1:])
        film.lisaFilm(y_filmi_nimi, y_žanr)
        print("Film lisatud!")
        return True
    elif tähis == "V":
        uus_y = y.split()
        y_filmi_nimi = " ".join(uus_y[1:])
        film.kustutaFilm(y_filmi_nimi)
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    elif tähis != "E":
        return True
    else:
        return False

print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:     L <žanr> <film>
Vaata filmi:  V <filmi nimi>
Lõpeta:       E
===""")

sisestus = list(map(str, input("> ").split()))
#https://prutor.ai/taking-multiple-inputs-from-user-in-python/
y = " ".join(sisestus[1:])
        
while töötleKäsk(sisestus[0], y) is True:
    sisestus = list(map(str, input("> ").split()))
    y = " ".join(sisestus[1:])