import film


järjend2 = []
ÜhtneJärjend = []
def töötleKäsk(sõne,järjend):
    i = 0
    if sõne == "K": # kui tahetakse filme kuvada
        järjend2 = film.loetleFilmid(järjend)
        print("Võimalikud filmid on: ")
        while i < len(järjend2):
            print(järjend2[i])
            i+=1
    elif sõne == "L": # Kui tahetakse filme lisada
        if len(ÜhtneJärjend)> 2:
            film.lisaFilm(ÜhtneJärjend[1:3],ÜhtneJärjend[0])
        else:
            film.lisaFilm(ÜhtneJärjend[1],ÜhtneJärjend[0])

        print("Film lisatud!")
    elif sõne == "V":
        film.kustutaFilm(ÜhtneJärjend[0])
        print("Film nimekirjat kustutatud!")
        print("Head vaatamist!")
        
käsud ="K L V E"
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")

while True:
    sisend = input("> ")
    sisend2 = sisend.split(" ")
    järjend2 = [sisend2]
    ÜhtneJärjend = sum(järjend2,[]) #Et input oleks ühes listis
    if ÜhtneJärjend[0] in käsud:
        if ÜhtneJärjend[0] == "K":
            töötleKäsk("K","multikas")
            
        elif ÜhtneJärjend[0] == "L":
            ÜhtneJärjend.remove("L")
            ÜhtneJärjend[1] += " "
            töötleKäsk("L",ÜhtneJärjend)
            
        elif ÜhtneJärjend[0] == "V":
            ÜhtneJärjend.remove("V")
            töötleKäsk("V",ÜhtneJärjend)
            
        elif sisend == "E":
            break
    
