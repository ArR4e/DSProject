def uuendaFilmid(kas_uuendad):
    nõustuv = "jah"
    eitav = "ei"
    if kas_uuendad == nõustuv:
        uus_film = input("Sisesta uue filmi nimi: ")
        uus_žanr = input("Sisesta uue filmi žanr: ")
        fail = open("näidis.txt", "a", encoding="UTF-8")
        fail.write(f"{uus_film} - {uus_žanr}" +"\n")
        fail.close()
    else:
        False

def loetleFilmid(žanr):
    järjend = []
    žanrid = []
    vastavfilm = []
    
    f = open("näidis.txt", encoding="UTF-8")
    for rida in f:
        rida = rida.strip()
        osad2 = rida.split(" - ")
        osad = rida.split(",")
        vastavžanr = osad2[1].split(",")
        järjend = järjend + osad
        žanrid = žanrid + vastavžanr
    f.close()
    
    while True:
        if žanr in žanrid:
            break
        else:
            print("Vastava žanriga filmi ei leidu andmebaasis, proovi uuesti.")
            žanr = input("Sisesta filmižanr, mida tahad vaadata: ")
    
    vastavfilm = []
    for filmiliik in järjend:
        if filmiliik.endswith(žanr):
            osa = filmiliik.split(" - ")
            film = osa[0].split(",")
            vastavfilm += film
            continue
    return vastavfilm


def lisaFilm(vastavfilm, žanr):
    fail = open("filmid.txt","w", encoding="UTF-8")
    for film in vastavfilm:
        fail.write(f"{film} - {žanr}" +"\n")
    fail.close()

def kustutaFilm(filminimi):
    with open("filmid.txt","r+") as fail:
        new_fail = fail.readlines()
        fail.seek(0)
        for rida in new_fail:
            if filminimi not in rida:
                fail.write(rida)
        fail.truncate()

kas_uuendad = input("Kas soovid andmebaasi lisada uut filmi (jah/ei)?: ")
uuendaFilmid(kas_uuendad)
žanr = input("Sisesta filmižanr, mida tahad vaadata: ")
lisaFilm((loetleFilmid(žanr)),žanr)
filminimi = input("Sisesta selle filmi nimi, mis sul on vastavast žanrist vaadatud: ")
kustutaFilm(filminimi)

