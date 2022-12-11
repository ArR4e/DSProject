import film

#järjend mis sisaldab käsu argumente
def töötleKäsk(käsu_tähis, järjend):
    global summa
    summa += 1
    if käsu_tähis == 'K':
        filmid =film.loetleFilmid(järjend)
        loetud = 1
        if filmid != []:
            tulemus = ""
            for film1 in filmid:
                film1 += '\n'
                film_sõnena = "".join(film1)
                tulemus += film_sõnena
            print("Võimalikud filmid on:")
            print(tulemus)
        else:
            print('Soovitud žanris pole hetkel filme, tee uus valik')  
        return True
    elif käsu_tähis == 'L':
        teeme_listiks_tagasi = järjend.split(" ")
        žanr = teeme_listiks_tagasi[0]
        filmi_nimi = " ".join(teeme_listiks_tagasi[1:])
        print(film.lisaFilm(filmi_nimi, žanr))
        return True
    elif käsu_tähis == 'V':
        print(film.kustutaFilm(järjend))
        print("Film nimekirjast kustutatud!")
        print('Head vaatamist!')
        return True
    if käsu_tähis == 'E':
        return False
    
summa = 0
if summa == 0:
    print("=== FILMIANDMEBAAS ===")
    print("Kuva filmid: K <žanr>")
    print("Lisa film: L <žanr> <film>")
    print("Vaata filmi: V <filmi nimi>")
    print("Lõpeta: E")
    print("===")
    
while True:
    listike = input("> ")
    listike2 = listike.split(" ")
    käsu_tähis = listike2[0]
    järjend = ' '.join(listike2[1:])
    if töötleKäsk(käsu_tähis, järjend) == False:
        break
    else:
        continue