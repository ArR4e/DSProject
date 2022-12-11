import film

print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>  
Lisa film:   L <žanr> <film> 
Vaata filmi: V <filmi nimi> 
Lõpeta:      E 
===""")

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        filmid = film.loetleFilmid(järjend)
        if filmid == []:
            print("Ei ole midagi sellest kategooriast :((((")
        else:
            print("Võimalikud filmid on:")
            for i in filmid:
                print(i)
        return True
    
    elif tähis == "L":
        uus_järjend = järjend. split()
        nimelist = uus_järjend[1:]
        nimi = " ".join(nimelist)
        filmid = film.lisaFilm(nimi, uus_järjend[0])
        print("Film lisatud!")
        return True
    
    elif tähis == "V":
        filmid = film.kustutaFilm(järjend)
        print("""Film nimekirjast kustutatud!
        Head vaatamist!""")
        return True
    
    elif tähis == "E":
        return False
    
sisend = input()        
while töötleKäsk(sisend[0], sisend[2:]) == True:
    sisend = input()
    töötleKäsk(sisend[0], sisend[2:])
    


