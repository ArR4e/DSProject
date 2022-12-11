# esimene funktsioon, avab faili, loeb, seejärel sulgeb faili.
def loetleFilmid(žanr):
    list_filmidest = []
    esialgne_f = open("filmid.txt", "r", encoding="UTF-8")
    for rida in esialgne_f.readlines():
        jupid = rida.strip().split(" - ")
        # return jupid
        nimi = jupid[0]
        žanri_liik = jupid[1]
        if žanr == žanri_liik:
            list_filmidest.append(nimi.strip())
    esialgne_f.close()
    return list_filmidest


# teine funktsioon, avab uuesti faili, loeb, täiendab, seejärel sulgeb faili.


def lisaFilm(nimi, žanr):
    film_koos_žanriga = ""
    uus_f = open("filmid.txt", "a", encoding="UTF-8")
    uus_film = "\n" + nimi + " - " + žanr
    uus_f.write(uus_film)
    uus_f.close()


# kolmas funktsioon, avab faili, loeb, kontrollib, kustutab, seejärel sulgeb faili.


def kustutaFilm(nimi):
    uus_f = open("filmid.txt", "r", encoding="UTF-8")
    read = uus_f.readlines()
    uus_f.close()

    muutmiseks_f = open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        jupid = rida.strip().split(" - ")
        nimi = jupid[0]
        žanri_liik = jupid[1]
        if nimi != kustuta_film:
            muutmiseks_f.write(rida)
    muutmiseks_f.close()


küsi_žanr = input("Sisesta üks žanr: ")
print(loetleFilmid(küsi_žanr))

uus_filmi_nimi = input("Sisesta uus filmi nimi: ")
uus_filmi_žanr = input("Sisesta uue filmi žanr: ")
lisaFilm(uus_filmi_nimi, uus_filmi_žanr)
kustuta_film = input("Kustuta film: ")
kustutaFilm(kustuta_film)
