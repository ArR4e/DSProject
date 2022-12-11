import film
def töötlekäsk(käsu_tähis,järjend):
    if käsu_tähis.upper() == 'K':
        sisend = järjend
        print("Võimalikud filmid on: ")
        print(film.loetleFilmid(sisend))
        return True
    elif käsu_tähis.upper() == 'L':
        vahe_etapp = järjend.split(" ") 
        filmi_nimi = vahe_etapp[1]
        filmi_zanr = vahe_etapp[0]
        print(film.lisaFilm(filmi_nimi,filmi_zanr))
        print("Film lisatud!")
        return True
    elif käsu_tähis.upper() == 'V':
        sisu = järjend
        print("Film nimekirjast kustutatud!")
        print(film.kustutaFilm(sisu))
        print("Head vaatamist!")
        return True
    
    elif käsu_tähis.upper() == 'E':
        return False
    else:
        print("Vale sisend")




    
käsu_tähis = str(input("Sisesta käsk:"))
järjend= input("Sisesta käsu argumendid: ")

(töötlekäsk(käsu_tähis,järjend))

'''Koosta funktsioon töötleKäsk, millel on kaks parameetrit: käsu tähis ning järjend, mis sisaldab käsu
argumente. Funktsioon peab:

Käsu K puhul ekraanile väljastama nimekirja filmidest, mis on etteantud žanrist
Käsu L puhul lisama etteantud nime ja žanriga filmi faili
Käsu V puhul kustutama filmi failis olevast nimekirjast
Käsu E puhul tagastama tõeväärtuse False (teiste käskude puhul tagastatakse True).
Põhiprogrammis peab kasutaja saama käsurealt sisestada nelja käsklust järgmisel kujul:

 ​K <žanr>
 ​L <žanr> <filmi nimi>
 ​V <filmi nimi>
 ​E
Võib eeldada, et filmi žanri nimetus ei sisalda tühikuid.'''