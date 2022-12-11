from film import *

def töötleKäsk(a, käsud):
    if a == "K":
        print("Võimalikud filmid on:")
        kuvada = loetleFilmid(käsud[0])
        for i in kuvada:
            print(i)
        return True
        
    elif a == "L":
        nimes = käsud[1:]
        nimi = ""
        for i in nimes:
            nimi += i + " "
        nimi = nimi.strip()
        lisaFilm(nimi, käsud[0])
        print("Film lisatud!")
        return True
        
    elif a == "V":
        nimi = ""
        for i in käsud:
            nimi += i + " "
            
        nimi = nimi.strip()
        kustutaFilm(nimi)
        print("Film kustutatud!")
        print("Head vaatamist!")
        return True
        
    elif a == "E":
        return False
    
    
print("======== ANDMEBAAS =========")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <film>")
print("Lõpeta:      E")
print("============================")

sisend = ""

while True:
    valik = input("> ")
    valik = valik.split()
    sisend = valik[0]
    käsud = valik[1:]
    käsk = töötleKäsk(sisend, käsud)
    if  käsk == False:
        break
    
    
    