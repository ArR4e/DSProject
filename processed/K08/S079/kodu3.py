# 3. Juku filmiandmebaas
# Juku on suur filmisõber, kuid tal pole palju aega, et neid vaadata.
# Seega otsustas Juku koostada endale programmi, mis aitaks tal järge pidada heade filmide üle,
# et need tal meelest ära ei läheks. Kuna Jukul on vähe aega, loodab ta sealjuures, et ei pea
# kogu programmi koodi ise nullist kirjutama ja saab võimalikult palju olemasolevaid funktsioone ära kasutada.

# Aita Jukut ja kirjuta programm, mis ​võimaldab filme valida žanrite järgi.
# Programm peaks vajaminevad funktsioonid importima eelmises ülesandes loodud moodulist film (fail film.py).
# Pärast filmi valikut peab programm valitud filmi tekstifailist ära kustutama.
# Programm peab lubama ka soovi korral filme lisada. Kui tekstifailis pole soovitud žanrist ühtegi filmi,
# peab programm sellest teada andma ja andma uue võimaluse valikut teha.

# Koosta funktsioon töötleKäsk, millel on kaks parameetrit: käsu tähis ning järjend, mis sisaldab käsu argumente.
# Funktsioon peab:

# - Käsu K puhul ekraanile väljastama nimekirja filmidest, mis on etteantud žanrist
# - Käsu L puhul lisama etteantud nime ja žanriga filmi faili
# - Käsu V puhul kustutama filmi failis olevast nimekirjast
# - Käsu E puhul tagastama tõeväärtuse False (teiste käskude puhul tagastatakse True).
# - Põhiprogrammis peab kasutaja saama käsurealt sisestada nelja käsklust järgmisel kujul:

# ​K <žanr>
# ​L <žanr> <filmi nimi>
# ​V <filmi nimi>
# ​E
# Võib eeldada, et filmi žanri nimetus ei sisalda tühikuid.

# Näide programmi tööst

# >>> %Run nimi.py
# === FILMIANDMEBAAS ===
# Kuva filmid: K <žanr>
# Lisa film:   L <žanr> <film>
# Vaata filmi: V <filmi nimi>
# Lõpeta:      E
# ===
 
# > K märul
# Võimalikud filmid on:
# Avengers: End Game
# Spider-Man
 
# > L komöödia Borat
# Film lisatud!
 
# > V Avengers: End Game
# Film nimekirjast kustutatud!
# Head vaatamist!
 
# > E
# >>>
# Automaatkontroll. Programm impordib mooduli nimega film.
# Programmis peab olema kirjeldatud kahe argumendiga funktsioon töötleKäsk (arvesta suuri ja väikesi tähti).
# Funktsiooni esimene argument on sõne ning teine argument sõnedest koosnev järjend. Järjend võib ka tühi olla.
# Funktsioon väljastab ekraanile käsu tulemuse ja tagastab sobiva tõeväärtuse: False,
# kui programmi töö tuleks lõpetada ning vastasel juhul True. Põhiprogrammis peab kasutaja saama sisestada käsklusi,
# kusjuures käsklused peavad olema järgmisel kujul: esimesel kohal on käsu tähiseks olev täht,
# millele järgneb tühik ning seejärel tühikuga eraldatud argumendid.

from film import *

def töötleKäsk(käsk, *args):

  if käsk == "E":
    False

  elif käsk == "K":
      print("Võimalikud filmid on:")
      for film in filmid:
          print(film)

  elif käsk == "L":
        žanr = valikud[0]
        del valikud[0]
        nimi = " ".join(valikud)
        lisaFilm(nimi, žanr)
        print("Film lisatud!")

  elif käsk == "V":
        kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")

    
user_inp = input("=== FILMIANDMEBAAS ===\n"+
              "Kuva filmid: K <žanr>\n"+
              "Lisa film:   L <žanr> <film>\n"+
              "Vaata filmi: V <filmi nimi>\n"+
              "Lõpeta:      E\n"+
              "===\n")

while True:
    käsk = user_inp[0]
    valik = user_inp[2:]

    if käsk == "K":
        filmid = loetleFilmid(valik)
        if len(filmid) == 0:
              print("Pole sellise žanriga filmi. Vali uuesti.\n")
              user_inp = input("=== FILMIANDMEBAAS ===\n"+
              "Kuva filmid: K <žanr>\n"+
              "Lisa film:   L <žanr> <film>\n"+
              "Vaata filmi: V <filmi nimi>\n"+
              "Lõpeta:      E\n"+
              "===\n")
        else:
            töötleKäsk(käsk, valik)
            break
    elif käsk == "V":
        nimi = valik
        töötleKäsk(käsk, nimi)
        break
    else:
        valikud = valik.split()
        töötleKäsk(käsk, valikud)
        break

