import film
sisend = input("Sisesta käsu tähis ja argumendid: ")
sisendi_element = sisend.split(" ")
käsu_tähis = sisendi_element[0]
sisendi_element.remove(käsu_tähis)
argumentide_järjend = sisendi_element

def töötleKäsk(käsu_tähis,argumentide_järjend):
    
    if käsu_tähis == "K":
        zanri_nimi = argumentide_järjend[0]
        print(film.loetleFilmid(zanri_nimi))
        return True
        
    elif käsu_tähis == "L":
        zanr = argumentide_järjend[0]
        nimi = argumentide_järjend[1]
        film.lisaFilm(nimi,zanr)
        return True
    
    elif käsu_tähis == "V":
        Filmi_Nimi = argumentide_järjend[0]
        film.kustutaFilm(Filmi_Nimi)
        return True
    
    elif käsu_tähis == "E":
        return False

töötleKäsk(käsu_tähis,argumentide_järjend)
        