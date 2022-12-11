import film

def töötleKäsk(käsk, järjend):
    if käsk=="K":
        filmi_nimi=järjend[0]
        print(film.loetleFilmid(filmi_nimi))
        return True
    elif käsk=="L":
        filmi_nimi=" ".join(järjend[1:])
        žanr=järjend[0]
        film.lisaFilm(filmi_nimi,žanr)
        print("Film lisatud.")
        return True
    elif käsk=="V":
        filmi_nimi=" ".join(järjend)
        film.kustutaFilm(filmi_nimi)
        print("Film kustutatud.")
        return True
    elif käsk=="E":
        return False
    
while True:
    sisesta=input("Sisesta käsk:").split(" ")
    if not töötleKäsk(sisesta[0], sisesta[1:]):
        break   