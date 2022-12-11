from film import *

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")
    
def töötleKäsk(käsk, järjend):
    if käsk == "K":
        žanr = järjend[0].lower()
        filmid = loetleFilmid(žanr)
        if filmid == []:
            print("Sellist žanri filme pole!")
        else: 
            print("Võimalikud filmid on:")
            for film in filmid:
                print(film)
        return True
    elif käsk == "L":
        žanr = järjend[0].lower()
        nimi = " ".join(järjend[1:])
        lisaFilm(nimi, žanr)
        print("Film lisatud!")
        return True
    elif käsk == "V":
        nimi = " ".join(järjend[0:])
        kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!" + "\n" + "Head vaatamist")
        return True
    elif käsk == "E":
        return False

while True:
    sisend = input()
    i = sisend.find(" ")
    käsk = sisend[:1].strip()
    järjend = sisend[i+1:].split()
    if töötleKäsk(käsk, järjend) == False:
        break
    else:
        continue