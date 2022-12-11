import film

def töötleKäsk(tähis,järjend):
    if tähis == "K":
        filmid = film.loetleFilmid(järjend[0])
        print("Võimalikud filmid on:" + "\n" + str(filmid))
        return True
    elif tähis == "L":
        film.lisaFilm(järjend[1],järjend[0])
        print("Film lisatud!")
        return True
    elif tähis == "V":
        film.kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud!"+ "\n" + "Head vaatamist!")
        return True
    elif tähis == "E":
        return False
    
        
        
print("=== FILMIANDMEBAAS ===" + "\n" + "Kuva filmid: K <žanr>" + "\n"  "Lisa film:   L <žanr> <film>" + "\n" + "Vaata filmi: V <filmi nimi>" + "\n" + "Lõpeta:      E" + "\n" + "===")

järjend = []

while True:
    sisend = input("")
    tähis = sisend[0].upper()
    
    if tähis == "L" or tähis =="V":
        sisend = sisend.split(" ",2)
        sisend2 =int(len(sisend)) + 1
        järjend = sisend[1 : sisend2]
    else:
        sisend2 =int(len(sisend))
        järjend.append(sisend[2 : sisend2])
    
    if töötleKäsk(tähis,järjend) == False:
        break
         
