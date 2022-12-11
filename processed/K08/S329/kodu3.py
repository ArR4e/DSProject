# 3. Juku filmiandmebaas

import film

def töötleKäsk(käsu_tähis, järjend):
    if käsu_tähis == 'K':
        žanr = järjend
        with open('filmid.txt', encoding = "UTF-8") as file:
            fail = file.read()
            if žanr in fail.split():
                filmid = film.loetleFilmid(žanr)
                print("Võimalikud filmid on:")
                for el in filmid:
                    print(el)
                print("")
            else:
                print("Ma ei leidnud filmi žanrit. Proovige kirjutada midagi muud või kirjutada filmi nime õigesti!")
                print("")
        file.close()
    elif käsu_tähis == 'L':
        žanr = järjend[0]
        nimi = " ".join(järjend[1:])
        film.lisaFilm(nimi, žanr)
        print("Film lisatud!")
        print("")
    elif käsu_tähis == 'V':
        nimi = järjend
        with open('filmid.txt', encoding = "UTF-8") as file:
            fail = file.read()
            if nimi in fail:
                film.kustutaFilm(nimi)
                print("Film nimekirjast kustutatud!")
                print("Head vaatamist!")
                print("")
            else:
                print("Ma ei leidnud filmi nime. Proovige kirjutada midagi muud või kirjutada filmi nime õigesti!")
        file.close()
        
while True:
    n = input("Kirjutage käsk: ")
    m = n.split()
    print("")
    print("=== FILMIANDMEBAAS ===")
    if m[0] == 'K':
        print("Kuva filmid: " + n)
        print("===")
        print("")
        käsu_tähis = m[0]
        try:
            järjend = m[1]
        except:
            print("Vabandage mind! Ma ei saa leida filme!")
            print("")
            continue
        print("> " + n)
        töötleKäsk(käsu_tähis, järjend)
    elif m[0] == 'L':
        print("Lisa film: " + n)
        print("===")
        print("")
        käsu_tähis = m[0]
        try:
            järjend = m[1:]
        except:
            print("Vabandage mind! Ma ei saa nime ja žanri nimekirja lisada, sest need puuduvad!")
            print("")
            continue
        print("> " + n)
        töötleKäsk(käsu_tähis, järjend)
    elif m[0] == 'V':
        print("Vaata film: " + n)
        print("===")
        print("")
        käsu_tähis = m[0]
        try:
            järjend = ' '.join(m[1:])
        except:
            print("Vabandage mind! Ma ei saa konkreetset filmi nimekirjast eemaldada, sest see on puudu!")
            print("")
            continue
        print("> " + n)
        töötleKäsk(käsu_tähis, järjend)
    elif m[0] == 'E':
        print("Lõpeta: " + n)
        print("===")
        print("")
        print("> " + n)
        break
    
print("")