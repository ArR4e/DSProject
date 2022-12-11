import film

def töötleKäsk(käsu_tähis, tegevus):
    if käsu_tähis == "K":
        loetleFilmid(järjend[1])
    elif käsu_tähis == "L":
        lisaFilm()
    elif käsu_tähis == "V":
        kustutaFilm()
    elif käsu_tähis == "E":
        return False

print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film: L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta: E\n===")
while True:
    järjend = []
    sisestus = input("> ")
    järjend += sisestus.split(" ") #kui sisestatakse 3 sõna, mille vahel tühik, siis ei toimi, mõtle muud välja!
    käsu_tähis = järjend[0]
    tegevus = järjend[1]
    töötleKäsk(käsu_tähis, tegevus)
    