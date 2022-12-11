import film

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        print("Võimalikud filmid on: ")
        filmid = film.loetleFilmid(järjend)
        filminimi = "".join(map(str, filmid))
        print(str(filminimi) + "\n")
        return True
    elif tähis == "L":
        uus_järjend = järjend.split()
        film.lisaFilm(uus_järjend[1], uus_järjend[0])
        print("Film " + uus_järjend[1] + " on lisatud!" + "\n")
        return True
    elif tähis == "V":
        film.kustutaFilm(järjend)
        print("Film on nimekirjast kustutatud!")
        print("Head vaatamist!" + "\n")
        return True
    elif tähis == "E":
        return False
    
print("FILMIDEBAAS".center(30))
print("Kuva filmid:\tK <žanr>")
print("Lisa film:\tL <žanr> <film>")
print("Vaata filmi:\tV <filmi nimi>")
print("Lõpeta: \tE")

while True:
    tähis = input("Sisesta tähis: ")
    järjend = input("Sisesta vajalikud andmed: ")
    if tähis == "":
        print("Proovi uuesti!")
    if töötleKäsk(tähis, järjend) == False:
        break
