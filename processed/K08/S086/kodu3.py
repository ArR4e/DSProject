#Juku filmiandmebaas

#K <žanr> (list filmidest)
#​L <žanr> <filmi nimi> lisa film
#​V <filmi nimi> kustuta
#​E tagasta false, muidu true, sellega suletakse programm

import film

def töötleKäsk(tähis, argumendid):
    print(tähis)
    print(argumendid)
    if tähis in ["K", "L", "V"] and len(argumendid) == 0:
        print("Sisestatud käsk oli vigane. Proovi uuesti")
        return False
    
    if tähis == "K":
        print("Võimalikud filmid on:")
        filmid = film.loetleFilmid(argumendid[0])
        for nimi in filmid:
            print(nimi)
        return False
    
    elif tähis == "L":
        film.lisaFilm(argumendid[1], argumendid[0])
        print("Film lisatud")
        return False
    
    elif tähis == "V":
        film.kustutaFilm(argumendid[0])
        print("Film nimekirjast kustutatud")
        print("Head vaatamist!")
        return False
    
    elif tähis == "E":
        return True
    
    else:
        print("Sisestatud käsk oli vigane. Proovi uuesti")
        return False
    

print("======= FILMIANDMEBAAS =======\n")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("==============================\n")

while True:
    sisend = input().split(" ", 2) #"Lõikab" sisestatud käsust välja tähise ja žanri nimetuse (need ei sisalda tühikuid)
    käsk = sisend[0]
    parameetrid = sisend[1:]
    
    if töötleKäsk(käsk, parameetrid):
        break
    
    
    