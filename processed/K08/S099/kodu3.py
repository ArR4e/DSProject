import film

def töötleKäsk(sõne,järjend):
    if sõne.upper() == "K":
        zanr = järjend[0].lower()
        filmid = film.loetleFilmid(zanr)
        if filmid != [] and zanr.lower != "kõik":
            print("Võimalikud filmid on:")
            for film1 in filmid:
                print(film1)
        elif filmid == [] and zanr == "kõik":
            print("Filme ei leitud.")
        else:
            zanr = input("Selles žanris filme ei leitud. \nPalun sisesta mõni muu žanr: ")
            töötleKäsk("K",[zanr])
        return True
    elif sõne.upper() == "L":
        zanr = järjend[0].lower()
        if len(järjend) > 1:
            film1 = ""
            for i in range(1, len(järjend)):
                film1 += järjend[i] + " "
            film1 = film1.strip()
        else:
            film1 = järjend[1]
        film.lisaFilm(film1,zanr)
        print("Film lisatud!")
        return True
    elif sõne.upper() == "V":
        if len(järjend) > 1:
            film1 = ""
            for i in range(0, len(järjend)):
                film1 += järjend[i] + " "
            film1 = film1.strip()
        else:
            film1 = järjend[0]
        film.kustutaFilm(film1)
        print("Head vaatamist")
    elif sõne.upper() == "E":
        return False
    

print("""====== FILMIANDMEBAAS ======
Kuva filmid: K <žanr> 
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
============================""")
while True:
    käsk = input().split(" ")
    sõne = käsk[0]
    järjend = []
    if len(käsk) > 1:
        for i in range(1, len(käsk)):
            järjend += [käsk[i]]
    if töötleKäsk(sõne,järjend) == False:
        break
        
        
        

