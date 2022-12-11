# Juku filmiandmebaas

import film

def töötleKäsk(tähis, käsu_arg):
    if tähis == "K": # Loetleb filmid
        filmid = film.loetleFilmid(käsu_arg[0])
        if len(filmid) == 0:
            print("Filmiandmebaasis ei ole sisestatud žanriga filme.")
            žanr = input("Sisestage uus žanr: ")
            töötleKäsk("K", [žanr])
        else:
            print("Võimalikud filmid on: " + "\n")
            for i in filmid:
                print(i)
        return True

    elif tähis == "L": # Lisab filmi
        film.lisaFilm(" ".join(käsu_arg[1:]), käsu_arg[0])
        return True

    elif tähis == "V": # Kustutab filmi
        film.kustutaFilm(käsu_arg[0])
        return True

    elif tähis == "E": # tagastab Falsi
        return False

print(" === FILMIANDMEBAAS ===" + "\n", "Kuva filmid: K <žanr>" + "\n", "Lisa film:   L <žanr> <film>" + "\n",
      "Vaata film:  V <filmi nimi>" + "\n", "Lõpeta:      E" + "\n", "===")

while True:
    sisend = input().split()
    if töötleKäsk(sisend[0], sisend[1:]):
        continue
    else:
        break