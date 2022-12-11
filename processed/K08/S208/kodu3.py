from film import *
def töötleKäsk(täht, arg):
    nimed = ""
    koos = ""
    n = ""
    m = ""
    for i in arg[1:]:
        nimed += m+i
        m = " "
    for i in arg:
        koos += n+i
        n = " "
    if täht == "E":
        return False
    elif täht == "K":
        print("Võimalikud filmid on:")
        k = loetleFilmid(arg[0])
        for i in k:
            print(i)
        return True
    elif täht == "V":
        kustutaFilm(koos)
        print("Film nimekirjast kustutatud!" + "\n" + "Head vaatamist!")
        return True
    elif täht == "L":
        lisaFilm(nimed, arg[0])
        return True
print(7*"="+" Filmiandmebaas "+7*"=" + "\n" + "Kuva filmid: K <žanr>" + "\n" + "Vaata filmi: V <filmi nimi>" + "\n" + "Lisa film:   L <žanr> <film>" + "\n" + "Lõpeta:      E" + "\n" + (30*"="))
try:
    while True:
        sis = input("> ").split(" ")
        täht = str(sis[0])
        arg = sis
        arg.remove(sis[0])
        if töötleKäsk(täht, arg) == False:
            break
except:
    pass