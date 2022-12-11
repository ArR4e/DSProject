import film

def töötle_käsk(käsu_tähis, järjend):
    if käsu_tähis == "K":
        if film.loetleFilmid(järjend[0]) == []:
            print("Kahjuks sellist žanri hetkel nimekirjas ei ole, proovi midagi muud.")
        else:
            print("Võimalikud filmid on: ")
            for rida in film.loetleFilmid(järjend[0]):
                print(rida)
        return True
    elif käsu_tähis == "L":
        nimi = ""
        for el in järjend[1:len(järjend)]:
            nimi += (el + " ")
        film.lisaFilm(nimi, järjend[0])
        print("Film lisatud!")
        return True
    elif käsu_tähis == "V":
        nimi = ""
        for el in järjend[0:len(järjend)]:
            nimi += (el + " ")
        film.kustutaFilm(nimi.rstrip())
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist")
        return True
    elif käsu_tähis == "E":
        return False

print("""=== FILMIANDMEBAAS ===    
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>    
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")
    
i = True
while i == True:
    sisend = input()
    sisendid = sisend.split(" ")
    käsu_tähis = sisendid[0].upper()
    järjend = sisendid[1:len(sisendid)]
    i = töötle_käsk(käsu_tähis, järjend)
    