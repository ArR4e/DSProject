from film import *

def töötleKäsk():

    print("=== FILMIANDMEBAAS ===")
    print("Kuva filmid: K <žanr>")
    print("Lisa film:   L <žanr> <film>")
    print("Vaata filmi: V <filmi nimi>")
    print("Lõpeta:      E")

    valik = input()

    if valik[0] == "k" or valik[0] == "K":
        print("Võimalikud filmid on:")
        filmid = loetleFilmid(valik[2:])
        for i in range(len(filmid)):
            print(filmid[i])
            
    """if valik[0] == "l" or valik[0] == "L":
        temp_valik = valik
        temp_valik = temp_valik[2:temp_valik.index(" ")]
        lisaFilm(valik[:temp_valik.index(" ")],nimi[temp_valik.index(" "):])"""

    if valik[0] == "V" or valik[0] == "v":
        print("Film nimekirjast kustutatud!")
        kustutaFilm(valik[2:])
        print("Head vaatamist!")
        
    if valik[0] == "e" or valik[0] == "E":
        exit()
    
    while valik[0] != "e" or valik[0] == "E":
        valik = input()

töötleKäsk()
