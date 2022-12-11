import film

print("=== FILMIANDMEBAAS ===" + "\n" + "Kuva filmid: " + "\t" + "K <žanr>")
print("Lisa film: " + "\t" + "L <žanr> <film>")
print("Vaata filmi: " + "\t" + "V <filmi nimi>")
print("Lõpeta: " + "\t" + "E")
print("===")

    
def töötleKäsk(tähis,järjend):
    
    if tähis == "K":
        žanr = järjend[-1]
        kuvatav = film.loetleFilmid(žanr)
        print("Võimalikud filmid on:")
        for i in kuvatav:
            print(i)
            
        return True
    
    if tähis == "L":
        žanr = järjend[0]
        filmi_nimi = järjend[1:]
        sõne = " ".join(filmi_nimi)
        lisatav = film.lisaFilm(sõne,žanr)
        print("Film lisatud!")
        
        return True
        
    if tähis == "V":
        filmi_nimi = " ".join(järjend)
        kustutatav = film.kustutaFilm(filmi_nimi)
        print("Film nimekirjast kustutatud!" + "\n" + "Head vaatamist!")
        
        return True
    
    if tähis == "E":
        
        return False
    
while True:
    sisend = input()
    järjendina = sisend.split()
    tähis = järjendina[0]
    järjend = järjendina[1:]
    
    x = töötleKäsk(tähis,järjend)
    
    if x == False:
        break
