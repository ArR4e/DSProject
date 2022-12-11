from film import *

def töötleKäsk(käsk, järj):
    
    if käsk == "E":
        return False
    elif käsk == "K":
        filmid = loetleFilmid(järj[0])
        if filmid == []:
            print("Sellest žanrist pole ühtegi filmi.")
            return True
        else:
            print(f"Võimalikud filmid žanrist '{järj[0]}' on: ")
            for i in range(len(filmid)):
                print(filmid[i])
            return True
    elif käsk == "L":
        nimi = ""
        for x in järj[1::]:
            nimi += x + " "
        lisaFilm(nimi.strip(), järj[0])
        print("Film lisatud!")
        return True
    elif käsk == "V":
        nimi = ""
        for x in järj:
            nimi += x + " "
        kustutaFilm(nimi.strip())
        print("Film nimekirjast kustutatud! \nHead vaatamist!")
        return True
    else:
        print("Tundmatu käsk!\nProovi uuesti!")
        return True
print("""====== FILMIANDMEBAAS ======
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
============================""")
while True:
    sisend = input().split()
    käsk = sisend[0]
    järj = sisend[1::]
    if not töötleKäsk(käsk, järj):
        break

# while töötleKäsk(käsk, järj):
#     sisend = input().split()
#     käsk = sisend[0]
#     järj = sisend[1::]
#     töötleKäsk(käsk, järj)
    