import film

def töötleKäsk(käsk, järjend):
    print('''
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
======================
''')
    while True:
        try:  
            kask = input("> ").split(" ",2)
            if kask[0] == "K":
                print(film.loetleFilmid(kask[1]))
            elif kask[0] == "L":
                film.lisaFilm(kask[2],kask[1])
            elif kask[0] == "V":
                film.kustutaFilm(kask[1])
            elif kask[0] == "E":
                return False
            else:
                print("Teadmatu käsk")
        except:
            print("Vigane käsk")
            
töötleKäsk("K", "krimi")