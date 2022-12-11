import film

def töötleKäsk(tähis, järjend):
    if tähis == "K":
         
        vastus = film.loetleFilmid(järjend[0])
        if vastus == []:
            print("Sobivaid filme ei leidu. Vali uuesti.")
        else:
            print("Võimalikud filmid on: ")
            for element in vastus:
                print(element)
        return True
    if tähis == "L":
        
        žanr = järjend[0]
        
        nimi = järjend[1:]
        nimi2= " ".join(nimi)
        film.lisaFilm(nimi2, žanr)
        print("Film lisatud")
        return True
    
    if tähis == "V":
        järjend = " ".join(järjend)
        
        film.kustutaFilm(järjend)
        print("Film on nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    if tähis == "E":
        return False
        
           
while True:
    käsk_sisestatud = input("Sisesta käsk: ")
    jaotus = käsk_sisestatud.split(" ")
    käsk = jaotus[0]
    järjend = jaotus[1:]

    if töötleKäsk(käsk,järjend) == False:
        break
    