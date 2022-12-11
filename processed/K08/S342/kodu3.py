from film import *
def töötleKäsk(käsk):
    käsusisu = käsk.split(" ")
    a = True
    if käsusisu[0] == "K":
        kuva = loetleFilmid(käsusisu[1])
        if kuva != []:
            print("Võimalikud filmid on:")
            for elem in kuva:
                print(elem)
        else:
            print("Sellise žanriga filme pole nimekirjas, proovi uuesti!")
        return True
    if käsusisu[0] == "L":
        lisaFilm(" ".join(käsusisu[2:]), käsusisu[1])
        print("Film lisatud!")
        return True
    if käsusisu[0] == "V":
        kustutaFilm(käsusisu[1])
        print("Film nimekirjast kustutatud!" + "\n" + "Head vaatamist!")
        return True
    if käsk == "E":
        return False
print("=== FILMIANDMEBAAS ===" +  "\n" + "Kuva filmid: K <žanr>" + "\n" + "Lisa film:   L <žanr> <film>" + "\n" + "Vaata filmi: V <filmi nimi>" + "\n" + "Lõpeta:      E" + "\n" + "===")
a = töötleKäsk(input())
while a == True:
    a = töötleKäsk(input())