import film

def töötleKäsk(k2sk, argument=None):
    if k2sk == "K":
        filmid = film.loetleFilmid(argument[0])
        if len(filmid) == 0:
            print("Selle žanri filme pole hetkel andmebaasis")
            return True
        else:
            print("Võimalikud filmid on:")
            print(filmid)
            return True
    elif k2sk == "L":
        film.lisaFilm(argument[1], argument[0])
        print("Film lisatud!")
        return True
    elif k2sk == "V":
        print(argument[0])
        film.kustutaFilm(argument[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    elif k2sk == "E":
        return False

while True:
    print("=== FILMIANDMEBAAS ===")
    print("Kuva filmid: K <žanr>")
    print("Lisa film:   L <žanr> <film>")
    print("Vaata filmi: V <filmi nimi>")
    print("Lõpeta:      E")
    print("===")
    valikud = input().split()
    k2sk = valikud[0]
    if str(k2sk) == "K":    
        argument = [valikud[1]]
        töötleKäsk(k2sk, argument)
    elif str(k2sk) == "L":
        nimi = valikud[2:len(valikud)]
        kokku = ""
        for sõna in nimi:
            kokku = kokku+sõna+" "
        kokku = kokku.strip()
        argument = [valikud[1], kokku]
        töötleKäsk(k2sk, argument)
    elif str(k2sk) == "V":
        nimi = valikud[1:len(valikud)]
        kokku = ""
        for sõna in nimi:
            kokku = kokku+sõna+" "
        kokku = kokku.strip()
        argument = [kokku]
        töötleKäsk(k2sk, argument)
    else:
        if not töötleKäsk(k2sk):
            break