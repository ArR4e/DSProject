import film
def töötleKäsk(un,dos="",tres=""):
    if un =="K":
        var = film.loetleFilmid(dos)
        if var!=[]:
            print("Võimalikud filmid on:")
            for x in var:
                print(x)
        else:
            print("Sellisest žanrist pole filme, proovi uuesti!")
        return True
    elif un=="L":
        film.lisaFilm(tres,dos)
        print("Film lisatud!")
        return True
    elif un =="V":
        film.kustutaFilm(dos)
        print("Film nimekirjast kustutatud! \n Head vaatamist!")
        return True
    elif un =="E":
        return False
    else:
        print("Väär käsk, proovi uuesti!")
        return True
def töötleja(imp):
    imp=imp.strip()
    #käsk
    un=imp[0]
    #ganre
    dos=""
    #nimi
    tres=""
    if un=="K":
        n=1
        dos=""
        for i in imp:
            if n>2:
                dos+=i
            n+=1
    elif un=="L":
        n=1
        trf=False
        for x in imp:
            if n>2:
                if trf:
                    tres+=x
                else:
                    if x ==" ":
                        trf=True
                    else:
                        dos+=x
            n+=1
    elif un=="V":
        n=1
        dos=""
        for i in imp:
            if n>2:
                dos+=i
            n+=1
    return töötleKäsk(un,dos,tres)
print("=== FILMIANDMEBAAS === \n Kuva filmid: K <žanr> \n Lisa film:   L <žanr> <film>\n Vaata filmi: V <filmi nimi> \n Lõpeta:      E \n ===")
while töötleja(input("> ")):
    pass