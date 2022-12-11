from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm

def töötleKäsk(tähis, järjend):
    if tähis == "E" and järjend == "":
        return False
    
    elif tähis == "K":
        filmid = loetleFilmid(järjend[0])
        if filmid == []:
            print("Sellist žanri filme ei leitud. Proovige uuesti.")
        else:
            print("Võimalikud filmid on:")
            for i in filmid:
                print(i)
        return True
            
    elif tähis == "L":
        nimi = " ".join(järjend[1:len(järjend)])
        lisaFilm(nimi, järjend[0])
        print("Film lisatud!")
        return True
        
    elif tähis == "V":
        nimi = " ".join(järjend[0:len(järjend)])
        kustutaFilm(nimi)
        print("Film nimekirjast kustutatud.")
        print("Head vaatamist!")
        return True
   
print("===FILMIANDMEBAAS===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")

while True:
    valik = input().split()
    if len(valik) == 1:
        tähis = valik[0]
        järjend = ""
    else:
        tähis = valik[0]
        järjend = valik[1:len(valik)]
    väärtus = töötleKäsk(tähis, järjend)
    
    if väärtus == True:
        continue
    else:
        break